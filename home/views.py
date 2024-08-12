from django.shortcuts import render
from books.models import Book


def home(request):
    # Get the top three most issued books
    top_books = Book.objects.order_by('-issued_times')[:3]

    context = {
        'top_books': top_books,
    }
    return render(request, 'home/home.html', context)
