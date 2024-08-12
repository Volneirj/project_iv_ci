from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta
from .models import IssuedBook
from books.models import Book


class IssuedBookModelTest(TestCase):

    def setUp(self):
        # Create a user and a book instance for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            isbn='1234567890123',
            description='A test book description.',
            available_copies=10
        )
        self.issued_book = IssuedBook.objects.create(
            book=self.book,
            user=self.user
        )

    def test_field_storage_and_retrieval(self):
        """
        Test that fields are correctly stored and retrieved.
        """
        issued_book = IssuedBook.objects.get(id=self.issued_book.id)
        self.assertEqual(issued_book.book, self.book)
        self.assertEqual(issued_book.user, self.user)
        self.assertEqual(issued_book.returned, False)
        self.assertTrue(issued_book.issue_date)
        self.assertAlmostEqual(
            issued_book.due_date,
            timezone.now() + timedelta(days=14),
            delta=timedelta(days=1)
        )

    def test_default_due_date(self):
        """
        Ensure the due_date is set to 14 days from
        the issue_date by default.
        """

        # Ensure both issue_date and due_date are timezone-aware
        issue_date = self.issued_book.issue_date
        expected_due_date = issue_date + timedelta(days=14)
        # calculate difference between the due_time caculated and the expected
        difference = self.issued_book.due_date - expected_due_date
        self.assertTrue(abs(difference.total_seconds()) < 10)

    def test_default_returned(self):
        """
        Verify that the returned field defaults to False.
        """
        self.assertFalse(self.issued_book.returned)

    def test_late_fee_calculation(self):
        """
        Test that the late_fee method calculates
        the correct fee when the book is returned late.
        """
        # Simulate a return date that is 5 days late
        return_date = self.issued_book.due_date + timedelta(days=5)
        self.issued_book.return_date = return_date
        self.issued_book.save()
        self.assertEqual(self.issued_book.late_fee(), 5)

    def test_no_late_fee(self):
        """
        Verify that the late_fee method returns 0
        if the book is returned on or before the due date.
        """
        # Return the book on time
        self.issued_book.return_date = self.issued_book.due_date
        self.issued_book.save()
        self.assertEqual(self.issued_book.late_fee(), 0)

    def test_edge_case_no_return_date(self):
        """
        Check that late_fee returns 0
        if there is no return_date (i.e., the book hasn't been returned).
        """
        self.issued_book.return_date = None
        self.issued_book.save()
        self.assertEqual(self.issued_book.late_fee(), 0)
