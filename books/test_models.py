from django.test import TestCase
from django.db import IntegrityError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from django.conf import settings
from .models import Book,BookSuggestion
import os
from cloudinary import CloudinaryImage

class BookModelTest(TestCase):

    # Set True to do the cloudinary upload image test
    test_cloud_image = False

    def setUp(self):
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            isbn='1234567890123',
            description='A test book description.',
            available_copies=10
        )

        # Ensure the test media directory exists
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)

    def test_string_representation(self):
        """
        Test that the __str__ method returns the expected string 
        representation of a Book instance
        """
        self.assertEqual(str(self.book), 'Test Book')

    def test_default_values(self):
        """
        Test that default values are correctly set for fields description, 
        available_copies,and issued_times when a book is created without 
        specifying these fields.
        """
        book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            isbn='1234567890125'
        )
        self.assertEqual(book.description, '')
        self.assertEqual(book.available_copies, 0)
        self.assertEqual(book.issued_times, 0)
    
    def test_isbn_unique(self):
        """
        Test that isbn field is unique.
        """
        with self.assertRaises(IntegrityError):
            Book.objects.create(
                title='Another Test Book',
                author='Another Author',
                isbn='1234567890123',  # Duplicate ISBN
                description='Another test book description.',
                available_copies=5
            )
    def test_isbn_field_data_type(self):
        """
        Test that the ISBN field correctly stores string values.
        """
        self.assertIsInstance(self.book.isbn, str)
        self.assertEqual(self.book.isbn, '1234567890123')
        
    def test_available_copies_cannot_be_negative(self):
        """
        Test that the available_copies field cannot be set to a negative value.
        """
        # Create a book instance with a negative available_copies value
        book = Book(
            title='Test Book',
            author='Test Author',
            isbn='1234567890123',
            description='A test book description.',
            available_copies=-1  # Invalid negative copies
        )
        
        # Attempt to save the book instance and check for validation error
        with self.assertRaises(ValidationError):
            book.full_clean()
        
    def test_available_copies_data_type(self):
        """
        Test that the available_copies field stores integer values correctly.
        """
        self.assertIsInstance(self.book.available_copies, int)
        self.assertEqual(self.book.available_copies, 10)

    def test_featured_image_default(self):
            """
            Test that the featured_image field has the default value when no image is provided.
            """
            book = Book.objects.create(
                title='Test Book',
                author='Test Author',
                isbn='1234567890128',
                description='A test book description.',
                available_copies=10
            )
            self.assertEqual(book.featured_image, 'placeholder')

    if test_cloud_image == True:
        def test_featured_image_upload(self):
            """
            Test that the featured_image field properly handles an uploaded image file.
            """

            with open('static/media/book_images/placeholder.jpg', 'rb') as image_file:
                image_content = image_file.read()

            # Create a small in-memory image file
            image_file = SimpleUploadedFile(
                'test_image.jpg',
                image_content,
                content_type='image/jpeg'
            )
            
            book = Book.objects.create(
                title='Test Book',
                author='Test Author',
                isbn='1234567890129',
                description='A test book description.',
                available_copies=10,
                featured_image=image_file
            )
                
            # Check if the image is correctly uploaded on Cloudinary
            self.assertTrue(book.featured_image.url)
            # Assert if URL contains a part of the image name
            self.assertIn('test_image', book.featured_image.url)

            # Using Cloudinary’s API to fetch the image metadata
            image = CloudinaryImage(book.featured_image.public_id)
            self.assertTrue(image)

    def test_book_creation(self):
        """
        Test that a new Book instance is saved correctly.
        """
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.isbn, '1234567890123')
        self.assertEqual(self.book.description, 'A test book description.')
        self.assertEqual(self.book.available_copies, 10)
        self.assertEqual(self.book.issued_times, 0)

    def test_book_update(self):
        """
        Test that updating an existing Book instance saves the changes correctly.
        """
        self.book.title = 'Updated Test Book'
        self.book.author = 'Updated Author'
        self.book.isbn = '9876543210987'
        self.book.description = 'An updated test book description.'
        self.book.available_copies = 15
        self.book.save()

        updated_book = Book.objects.get(id=self.book.id)
        self.assertEqual(updated_book.title, 'Updated Test Book')
        self.assertEqual(updated_book.author, 'Updated Author')
        self.assertEqual(updated_book.isbn, '9876543210987')
        self.assertEqual(updated_book.description, 'An updated test book description.')
        self.assertEqual(updated_book.available_copies, 15)

    def test_book_deletion(self):
        """
        Test that a Book instance is deleted correctly.
        """
        # Ensure the book exists before deletion
        self.assertTrue(Book.objects.filter(id=self.book.id).exists())
        
        # Delete the book
        self.book.delete()
        
        # Verify that the book has been deleted
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())


class BookSuggestionModelTest(TestCase):

    def setUp(self):
        """
        Create a BookSuggestion instance for testing.
        """
        self.suggestion = BookSuggestion.objects.create(
            book_title='Test Book Title',
            author='Test Author',
            name='Test Name',
            email='test@example.com',
            reason='Test reason for suggestion.'
        )

    def test_string_representation(self):
        """
        Test the string representation of the BookSuggestion model.
        """
        self.assertEqual(str(self.suggestion), 'Test Book Title')

    def test_field_data_types_and_constraints(self):
        """
        Test the data types and constraints of the BookSuggestion model fields.
        """
        self.assertEqual(self.suggestion.book_title, 'Test Book Title')
        self.assertEqual(self.suggestion.author, 'Test Author')
        self.assertEqual(self.suggestion.name, 'Test Name')
        self.assertEqual(self.suggestion.email, 'test@example.com')
        self.assertEqual(self.suggestion.reason, 'Test reason for suggestion.')

    def test_default_value_of_submitted_at(self):
        """
        Test that the submitted_at field is automatically set to the current date and time.
        """
        self.assertIsNotNone(self.suggestion.submitted_at)

    def test_field_constraints(self):
        """
        Test constraints like length and email format.
        """
        # Check book_title length constraint
        long_title = 'x' * 101
        suggestion = BookSuggestion(
            book_title=long_title,
            author='Test Author',
            reason='Test reason for suggestion.'
        )
        with self.assertRaises(ValidationError):
            suggestion.full_clean()

        # Check author length constraint
        long_author = 'x' * 101
        suggestion = BookSuggestion(
            book_title='Test Book Title',
            author=long_author,
            reason='Test reason for suggestion.'
        )
        with self.assertRaises(ValidationError):
            suggestion.full_clean()

        # Check valid email format
        invalid_email = 'blablabla'
        suggestion = BookSuggestion(
            book_title='Test Book Title',
            author='Test Author',
            email=invalid_email,
            reason='Test reason for suggestion.'
        )
        with self.assertRaises(ValidationError):
            suggestion.full_clean()

    def test_model_save_behavior(self):
        """
        Test that saving a BookSuggestion instance correctly updates the database.
        """
        suggestion = BookSuggestion.objects.create(
            book_title='Another Test Title',
            author='Another Author',
            name='Another Name',
            email='another@example.com',
            reason='Another reason for suggestion.'
        )
        self.assertEqual(BookSuggestion.objects.count(), 2)
        self.assertEqual(BookSuggestion.objects.get(id=suggestion.id).book_title, 'Another Test Title')