from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from cloudinary.models import CloudinaryField

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField(default='')
    featured_image = CloudinaryField('image', default='placeholder')
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title