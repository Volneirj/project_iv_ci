from django import forms
from .models import Book, BookSuggestion

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


class BookSuggestionForm(forms.Form):
    book_title = forms.CharField(
        max_length=100, 
        label='Book Title',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    author = forms.CharField(
        max_length=100, 
        label='Author',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    name = forms.CharField(
        max_length=100, 
        required=False, 
        label='Your Name (Optional)',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=False, 
        label='Email (Optional)',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), 
        label='Reason for Suggestion'
    )