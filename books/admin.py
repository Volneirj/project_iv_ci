from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Book

@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    """
    BookAdmin is a custom admin class for managing Book objects in the Django admin interface.
    """
    list_display = ('title', 'author', 'isbn', 'available_copies','issued_times')
    search_fields = ['title']
    list_filter = ('available_copies',)
    summernote_fields = ('description',)
