from django.urls import path
from .views import issue_book, issued_books_list, return_book


urlpatterns = [
    path('issue/<int:book_id>/', issue_book, name='issue_book'),
    path('list/', issued_books_list, name='issued_books_list'),
    path('return/<int:issued_book_id>/', return_book, name='return_book'),
]
