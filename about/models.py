from django.db import models

class BookSuggestion(models.Model):
    book_title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    reason = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_title
