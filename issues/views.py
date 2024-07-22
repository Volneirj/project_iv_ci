from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from .models import IssuedBook
from .forms import IssueBookForm
from books.models import Book

@login_required
def issue_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

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
            book.save()
            return redirect('book_detail', book_id=book_id)
    else:
        form = IssueBookForm(initial={'book_id': book_id})

    context = {
        'form': form,
        'book': book,
        'due_date': datetime.now() + timedelta(days=14)
    }

    return render(request, 'issues/issue_book.html', context)

@login_required
def issued_books_list(request):
    issued_books = IssuedBook.objects.filter(user=request.user)
    return render(request, 'issues/issued_books_list.html', {'issued_books': issued_books})
