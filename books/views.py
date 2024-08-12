from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Book, BookSuggestion
from .forms import BookForm, BookSuggestionForm


def book_list(request):
    """
    Displays a list of books, with optional search
    functionality and pagination.

    Returns:
        HttpResponse: The rendered book list page
        with the list of books, search query, and pagination.
    """
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
    """
    Displays the details of a specific book.

    Args:
        book_id: The ID of the book to display.

    Returns:
        HttpResponse: The rendered book detail page with the book's details.
    """
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book})


def is_admin(user):
    """
    Checks if a user is an admin.

    Args:
        user: The user to check.

    Returns:
        bool: True if the user is an admin, False otherwise.
    """
    return user.is_superuser


# Book CRUD front-end logic
@login_required
@user_passes_test(is_admin)
def book_create(request):
    """
    Handles the creation of a new book. Only accessible by admin users.

    Returns:
        HttpResponse: The rendered book creation form,
        or a redirect to the book list upon successful creation.
    """
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(
        request, 'books/book_form.html',
        {'form': form, 'title': 'Add Book'}
    )


@login_required
@user_passes_test(is_admin)
def book_update(request, book_id):
    """
    Handles the update of an existing book. Only accessible by admin users.

    Args:
        book_id: The ID of the book to update.

    Returns:
        HttpResponse: The rendered book update form,
        or a redirect to the book detail page upon successful update.
    """
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(
        request,
        'books/book_form.html',
        {'form': form, 'title': 'Update Book'}
    )


@login_required
@user_passes_test(is_admin)
def book_delete(request, book_id):
    """
    Handles the deletion of an existing book.
    Only accessible by admin users.

    Args:
        book_id: The ID of the book to delete.

    Returns:
        HttpResponse: The rendered book deletion confirmation page,
        or a redirect to the book list upon successful deletion.
    """
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})


def suggest_book_view(request):
    """
    Handles the submission of a book suggestion by users.

    Returns:
        HttpResponse: The rendered book suggestion form,
        or a redirect to the thank you page upon successful
        submission.
    """
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
    """
    Decorator that ensures the user is an admin.
    """
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    return decorated_view_func


@admin_required
def view_suggestions(request):
    """
    Displays a list of book suggestions. Only accessible by admin users.

    Returns:
        HttpResponse: The rendered book suggestions list page.
    """
    suggestions = BookSuggestion.objects.all()
    return render(
        request, 'books/view_suggestions.html',
        {'suggestions': suggestions}
    )


def thank_you_view(request):
    """
    Displays a thank you page after a book suggestion is submitted.
    """
    return render(request, 'books/thank_you.html')
