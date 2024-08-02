from django.db import models
from cloudinary.models import CloudinaryField

class Book(models.Model):
    """
    Represents a book in the library system.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The unique ISBN number of the book.
        description (str): A brief description of the book.
        featured_image (CloudinaryField): An image representing the book's cover.
        available_copies (int): The number of available copies of the book.
        issued_times (int): The number of times the book has been issued.
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField(default='')
    featured_image = CloudinaryField('image', default='placeholder')
    available_copies = models.PositiveIntegerField(default=0)
    issued_times = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
class BookSuggestion(models.Model):
    """
    Model to save the information in the database when someone suggest a book
    through the form

    Attributes:
        book_title (str): The title of the suggested book.
        author (str): The author of the suggested book.
        name (str): The name of the person suggesting the book (optional).
        email (str): The email of the person suggesting the book (optional).
        reason (str): The reason for suggesting the book.
        submitted_at (datetime): The date and time when the suggestion was submitted.
    """
    book_title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    reason = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_title
