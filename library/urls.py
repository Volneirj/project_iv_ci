from django.urls import path
from .views import home, book_list, book_detail, signup, issue_book

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('signup/', signup, name='signup'),
    path('issue_book/', issue_book, name='issue_book'),
]