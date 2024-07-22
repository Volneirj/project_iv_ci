from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Book, IssuedBook
from .forms import BookSearchForm, IssueBookForm, BookForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'library/signup.html', {'form': form})

def home(request):
    return render(request, 'library/home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

# def book_list(request):
#     form = BookSearchForm()
#     query = request.GET.get('query')
#     if query:
#         books = Book.objects.filter(title__icontains=query)
#     else:
#         books = Book.objects.all()
#     return render(request, 'library/book_list.html', {'books': books, 'form': form})

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
            print(f"Issued book: {issued_book}")
            return redirect('book_detail', book_id=book_id)
        else:
            print("Form is not valid") 
    else:
        form = IssueBookForm(initial={'book_id': book_id})

    context = {
        'form': form,
        'book': book,
        'due_date': datetime.now() + timedelta(days=14)
    }

    return render(request, 'library/issue_book.html', context)

@login_required
def issued_books_list(request):
    issued_books = IssuedBook.objects.filter(user=request.user)
    return render(request, 'library/issued_books_list.html', {'issued_books': issued_books})

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form, 'title': 'Add Book'})

@login_required
@user_passes_test(is_admin)
def book_update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form, 'title': 'Update Book'})

@login_required
@user_passes_test(is_admin)
def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'library/book_confirm_delete.html', {'book': book})


