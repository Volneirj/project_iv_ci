from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Book

@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available_copies')
    search_fields = ['title']
    list_filter = ('available_copies',)
    summernote_fields = ('description',)
