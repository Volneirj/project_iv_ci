from django import forms
from .models import IssuedBook

class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search Books', max_length=255)



class IssueBookForm(forms.ModelForm):
    class Meta:
        model = IssuedBook
        fields = ['book', 'user']