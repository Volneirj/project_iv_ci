from django.shortcuts import render
from books.models import Book
from django.db.models import Count

def home(request):
    # Annotate each book with the count of related issues
    top_books = Book.objects.annotate(issue_count=Count('title')).order_by('-issue_count')[:3]

    context = {
        'top_books': top_books,
    }
    return render(request, 'home/home.html', context)