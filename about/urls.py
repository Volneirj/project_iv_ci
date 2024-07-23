from django.urls import path
from .views import about_view, suggest_book_view, view_suggestions, thank_you_view

urlpatterns = [
    path('', about_view, name='about'),
    path('suggest_book/', suggest_book_view, name='suggest_book'),
    path('view_suggestions/', view_suggestions, name='view_suggestions'),
    path('thank_you/', thank_you_view, name='thank_you'),
]