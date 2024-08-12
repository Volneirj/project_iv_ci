from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta
from books.models import Book


class IssuedBook(models.Model):
    """
    IssuedBook model represents the record of a book issued
    to a user in the library system.

    Attributes:
    book (ForeignKey): indicating which book is issued.
    user (ForeignKey): indicating which user has issued the book.
    issue_date (DateTimeField): The date when the book was issued.
    return_date (DateTimeField): The date when the book was returned.
    due_date (DateTimeField): The date by which the book should be returned.
    returned (BooleanField): A flag indicating if book has been returned.

    Methods:
        __str__():
        Returns a string representation of the issued book and user.
        late_fee():
        Calculates and returns the late fee based on
        the return date and due date.
    """
    book = models.ForeignKey(Book,
                             related_name='issued_books',
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             related_name='issued_books',
                             on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(
        default=timezone.now() + timedelta(days=14))
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} issued to {self.user.username}"

    def late_fee(self):
        """
        Calculates the late fee for the issued book.

        If the book is returned after the due date,
        the late fee is calculated based on the number of days late.
        The daily fee is set to $1.

        Returns:
            int: The total late fee based on the number of days late.
        """
        daily_fee = 1
        if self.return_date and self.return_date > self.due_date:
            days_late = (self.return_date - self.due_date).days
            return days_late * daily_fee
        return 0
