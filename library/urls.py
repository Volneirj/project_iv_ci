from django.urls import path
from .views import home, book_list, book_detail, signup, issue_book, issued_books_list

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('books/<int:book_id>/issue/', issue_book, name='issue_book'),
    path('signup/', signup, name='signup'),
    path('issued_books/', issued_books_list, name='issued_books_list'),
]
