from django.db import models
from cloudinary.models import CloudinaryField

class Book(models.Model):
    """
    Book represents a book in the library system.
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
    book_title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    reason = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_title
