from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'description', 'featured_image', 'available_copies']

        #Garantee not add negative amount of books
        def clean_available_copies(self):
            available_copies = self.cleaned_data.get('available_copies')
            if available_copies < 0:
                raise forms.ValidationError("Available copies cannot be negative.")
            return available_copies
