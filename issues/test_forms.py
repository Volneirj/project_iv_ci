from django.test import TestCase
from django.utils import timezone
from .forms import IssueBookForm
from datetime import datetime, timedelta


class IssueBookFormTest(TestCase):

    def test_form_validity(self):
        """
        Test that the form is valid when provided with
        correct data for book_id and due_date.
        """
        form_data = {
            'book_id': 1,
            'due_date': datetime.now() + timedelta(days=14)
        }
        form = IssueBookForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_default_due_date(self):
        """
        Test that the default due_date is set to 14 days
        from the current date.
        """
        form = IssueBookForm()
        default_due_date = datetime.now() + timedelta(days=14)
        # Check if the default due_date is close to the expected date
        self.assertAlmostEqual(form.initial['due_date'],
                               default_due_date,
                               delta=timedelta(seconds=1))
