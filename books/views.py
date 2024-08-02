from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Book, BookSuggestion
from .forms import BookForm, BookSuggestionForm


def book_list(request):
    # Get the search query from the GET parameters
    query = request.GET.get('q', '')

    # Filter books based on the search query
    books = Book.objects.filter(title__icontains=query).order_by('title')

    # Set up pagination
    paginator = Paginator(books, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': query,
    }

    return render(request, 'books/book_list.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser

# Book CRUD front-end logic 
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
    return render(request, 'books/book_form.html', {'form': form, 'title': 'Add Book'})

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
    return render(request, 'books/book_form.html', {'form': form, 'title': 'Update Book'})

@login_required
@user_passes_test(is_admin)
def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

def suggest_book_view(request):
    if request.method == 'POST':
        form = BookSuggestionForm(request.POST)
        if form.is_valid():
            BookSuggestion.objects.create(
                book_title=form.cleaned_data['book_title'],
                author=form.cleaned_data['author'],
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                reason=form.cleaned_data['reason']
            )
            return redirect('thank_you')
    else:
        form = BookSuggestionForm()

    return render(request, 'books/suggest_book.html', {'form': form})

def admin_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    return decorated_view_func

@admin_required
def view_suggestions(request):
    suggestions = BookSuggestion.objects.all()
    return render(request, 'books/view_suggestions.html', {'suggestions': suggestions})

def thank_you_view(request):
    return render(request, 'books/thank_you.html')