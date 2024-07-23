from django.contrib import admin
from .models import BookSuggestion

@admin.register(BookSuggestion)
class BookSuggestionAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'author', 'name', 'email', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('book_title', 'author', 'name', 'email')
