from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Book, IssuedBook

@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'isbn', 'available_copies')
    search_fields = ['title']
    list_filter = ('available_copies',)
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(IssuedBook)