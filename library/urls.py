from django.urls import path
from .views import home, book_list, book_detail, signup

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='book_list'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('signup/', signup, name='signup'),
]