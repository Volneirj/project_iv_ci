from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from django import forms

class SuggestBookViewTests(TestCase):
    @patch('about.forms.SuggestBookForm')
    def test_suggest_book_form_valid(self, MockSuggestBookForm):
        # Mock form instance and its methods
        mock_form = MockSuggestBookForm.return_value
        mock_form.is_valid.return_value = True  # Simulate valid form
        mock_form.cleaned_data = {
            'book_title': 'Mock Book Title',
            'author': 'Mock Author',
            'name': 'Mock User',
            'email': 'user@example.com',
            'reason': 'Mock reason for suggesting the book.'
        }
        
        response = self.client.post(reverse('suggest_book'), data={
            'book_title': 'Mock Book Title',
            'author': 'Mock Author',
            'name': 'Mock User',
            'email': 'user@example.com',
            'reason': 'Mock reason for suggesting the book.'
        })

        # Check if the form was instantiated and is_valid was called
        MockSuggestBookForm.assert_called_once_with(data={
            'book_title': 'Mock Book Title',
            'author': 'Mock Author',
            'name': 'Mock User',
            'email': 'user@example.com',
            'reason': 'Mock reason for suggesting the book.'
        })
        mock_form.is_valid.assert_called_once()

        # Verify the response redirects or renders the correct template
        self.assertEqual(response.status_code, 302)

    @patch('yourapp.forms.SuggestBookForm')
    def test_suggest_book_form_invalid(self, MockSuggestBookForm):
        # Mock form instance and its methods
        mock_form = MockSuggestBookForm.return_value
        mock_form.is_valid.return_value = False  # Simulate invalid form

        response = self.client.post(reverse('suggest_book'), data={
            'book_title': '',
            'author': '',
            'name': '',
            'email': '',
            'reason': ''
        })

        # Check if the form was instantiated and is_valid was called
        MockSuggestBookForm.assert_called_once()
        mock_form.is_valid.assert_called_once()

        # Verify the response contains the form errors
        self.assertEqual(response.status_code, 200)  # Assuming rendering of the form on invalid submission
        self.assertContains(response, 'This field is required')  # Example of checking for form errors