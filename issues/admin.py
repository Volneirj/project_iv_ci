from django.contrib import admin
from .models import IssuedBook

@admin.register(IssuedBook)
class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'issue_date', 'due_date', 'returned')
    list_filter = ('returned', 'issue_date', 'due_date')
