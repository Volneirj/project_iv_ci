from django import forms
from datetime import datetime, timedelta


class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search Books', max_length=255)


class IssueBookForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput)
    due_date = forms.DateTimeField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initial['due_date'] = datetime.now() + timedelta(days=14)