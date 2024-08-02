from django import forms
from .models import Book, BookSuggestion

class BookForm(forms.ModelForm):
    """
    A form for creating and updating Book instances.

    Meta:
        fields (list): The fields of the model that will be included in the form.
    
    Methods:
        clean_available_copies: Validates that the available_copies field is not negative.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'description', 'featured_image', 'available_copies']

        def clean_available_copies(self):
            """
            Ensures that the number of available copies is not negative.

            Raises:
                forms.ValidationError: If the available_copies value is negative.
            
            Returns:
                int: The validated number of available copies.
            """
            available_copies = self.cleaned_data.get('available_copies')
            if available_copies < 0:
                raise forms.ValidationError("Available copies cannot be negative.")
            return available_copies


class BookSuggestionForm(forms.Form):
    """
    A form for suggesting new books to be added to the library.

    Fields:
        book_title (CharField): The title of the suggested book.
        author (CharField): The author of the suggested book.
        name (CharField): The name of the person suggesting the book (optional).
        email (EmailField): The email of the person suggesting the book (optional).
        reason (CharField): The reason for suggesting the book.
    """
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