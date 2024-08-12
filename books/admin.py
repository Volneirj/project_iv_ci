from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Book, BookSuggestion


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'author',
        'isbn',
        'available_copies',
        'issued_times'
    )
    search_fields = ['title']
    list_filter = ('available_copies',)
    summernote_fields = ('description',)


@admin.register(BookSuggestion)
class BookSuggestionAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'author', 'name', 'email', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('book_title', 'author', 'name', 'email')
