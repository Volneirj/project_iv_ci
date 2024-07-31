from django import forms
from datetime import datetime, timedelta

class IssueBookForm(forms.Form):
    """
    IssueBookForm is a Django form used for issuing a book to a user.

    Attributes:
        book_id (int): The ID of the book being issued. This field is hidden.
        due_date (datetime): The date and time when the book is due to be returned.

    The form automatically sets the initial due date to 14 days from the current date.
    """
    book_id = forms.IntegerField(widget=forms.HiddenInput)
    due_date = forms.DateTimeField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['due_date'] = datetime.now() + timedelta(days=14)
