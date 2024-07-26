from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, timedelta
from .models import IssuedBook
from .forms import IssueBookForm
from books.models import Book

@login_required
def issue_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    #Warn user has no available copies
    if book.available_copies <= 0:       
        messages.error(request, "Sorry, this book is out of stock and cannot be issued.")
        return redirect('book_list')

    # Check how many books the user has already issued
    issued_books_count = IssuedBook.objects.filter(user=request.user).count()
    issue_limit = 3  # Set the limit here

    if issued_books_count >= issue_limit:
        messages.error(request, f"You have reached your limit of "
                       f"{issue_limit} issued books. Please return it to issue a new one.")
        return redirect('book_list')  # Redirect to a page where the user can see the books

    # Issue the book
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            due_date = form.cleaned_data['due_date']
            issued_book = IssuedBook.objects.create(
                book=book,
                user=request.user,
                issue_date=timezone.now(),
                due_date=due_date
            )
            book.available_copies -= 1
            book.issued_times += 1
            book.save()
            return redirect('book_detail', book_id=book_id)
    else:
        form = IssueBookForm(initial={'book_id': book_id})
    
    context = {
        'form': form,
        'book': book,
        'due_date': datetime.now() + timedelta(days=14)
    }

    messages.success(request, "Book issued successfully!")
    return render(request, 'issues/issue_book.html', context)

@login_required
def issued_books_list(request):
    issued_books = IssuedBook.objects.filter(user=request.user).order_by('-issue_date')

    paginator = Paginator(issued_books, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'issues/issued_books_list.html', {'page_obj': page_obj})

@login_required
def return_book(request, issued_book_id):
    issued_book = get_object_or_404(IssuedBook, id=issued_book_id, returned=False)
    
    if request.method == 'POST':
        if 'confirm' in request.POST:
            # Confirm return and update the record
            issued_book.returned = True
            issued_book.return_date = timezone.now()

            # Increment the available copies of the book
            book = issued_book.book
            book.available_copies += 1
            book.save()

            issued_book.save()

            return redirect('issued_books_list') 
        
        elif 'cancel' in request.POST:
            return redirect('issued_books_list') 

    return render(request, 'issues/return_book_confirm.html', {'issued_book': issued_book})