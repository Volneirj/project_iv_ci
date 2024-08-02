from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import IssuedBook

@admin.register(IssuedBook)
class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'issue_date', 'due_date', 'returned')
    list_filter = ('returned', 'issue_date', 'due_date')

class UserAdmin(BaseUserAdmin):
    def issued_books_count(self, obj):
        count = IssuedBook.objects.filter(user=obj, returned=False).count()
        return format_html('<b>{}</b>', count)
    issued_books_count.short_description = 'Issued Books Count'

    # Modify the list display to include issued books count
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'issued_books_count')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
