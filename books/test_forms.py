from django.test import TestCase
from .models import BookSuggestion, Book
from .forms import BookSuggestionForm, BookForm


class BookSuggestionModelTest(TestCase):
    def test_book_suggestion_creation(self):
        """
        Test that a BookSuggestion instance is created and saved correctly.
        """
        suggestion = BookSuggestion.objects.create(
            book_title="Sample Book",
            author="Author Name",
            name="Test User",
            email="test@example.com",
            reason="This is a test suggestion."
        )
        self.assertEqual(str(suggestion), suggestion.book_title)
        self.assertEqual(suggestion.book_title, "Sample Book")
        self.assertEqual(suggestion.author, "Author Name")
        self.assertEqual(suggestion.name, "Test User")
        self.assertEqual(suggestion.email, "test@example.com")
        self.assertEqual(suggestion.reason, "This is a test suggestion.")


class BookSuggestionFormTest(TestCase):
    def test_valid_form(self):
        """
        Test that the form is valid with correct data.
        """
        form_data = {
            'book_title': 'Sample Book',
            'author': 'Author Name',
            'name': 'Test User',
            'email': 'test@example.com',
            'reason': 'This is a test suggestion.'
        }
        form = BookSuggestionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_title(self):
        """
        Test that the form is invalid with incorrect data.
        """
        form_data = {
            'book_title': '',
            'author': 'Author Name',
            'name': 'Test User',
            'email': 'test@example.com',
            'reason': 'This is a test suggestion.'
        }
        form = BookSuggestionForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_author(self):
        """
        Test that the form is invalid with incorrect data.
        """
        form_data = {
            'book_title': 'Sample Book',
            'author': '',
            'name': 'Test User',
            'email': 'test@example.com',
            'reason': 'This is a test suggestion.'
        }
        form = BookSuggestionForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_author_reason(self):
        """
        Test that the form is invalid with incorrect data.
        """
        form_data = {
            'book_title': 'Sample Book',
            'author': 'Author Name',
            'name': 'Test User',
            'email': 'test@example.com',
            'reason': ''
        }
        form = BookSuggestionForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_submission(self):
        """
        Test the form submission and saving to the database.
        """
        form_data = {
            'book_title': 'Sample Book',
            'author': 'Author Name',
            'name': 'Test User',
            'email': 'test@example.com',
            'reason': 'This is a test suggestion.'
        }
        form = BookSuggestionForm(data=form_data)
        self.assertTrue(form.is_valid())

        if form.is_valid():
            BookSuggestion.objects.create(
                book_title=form.cleaned_data['book_title'],
                author=form.cleaned_data['author'],
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                reason=form.cleaned_data['reason']
            )

        self.assertEqual(BookSuggestion.objects.count(), 1)
        suggestion = BookSuggestion.objects.first()
        self.assertEqual(suggestion.book_title, 'Sample Book')
        self.assertEqual(suggestion.author, 'Author Name')
        self.assertEqual(suggestion.name, 'Test User')
        self.assertEqual(suggestion.email, 'test@example.com')
        self.assertEqual(suggestion.reason, 'This is a test suggestion.')


class BookFormTest(TestCase):

    def test_valid_book_form(self):
        """
        Test that the BookForm is valid with all
        required fields correctly filled.
        """
        form_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'isbn': '1234567890123',
            'description': 'A test book description.',
            'available_copies': 10
        }
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_negative_available_copies(self):
        """
        Test that the BookForm is invalid if the available_copies is negative.
        """
        form_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'isbn': '1234567890123',
            'description': 'A test book description.',
            'available_copies': -1  # Invalid negative copies
        }
        form = BookForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('available_copies', form.errors)
        self.assertEqual(
            form.errors['available_copies'],
            ["Ensure this value is greater than or equal to 0."]
            )

    def test_blank_fields(self):
        """
        Test that the BookForm is invalid if required fields are left blank.
        """
        form_data = {
            'title': '',
            'author': '',
            'isbn': '',
            'description': '',
            'available_copies': ''
        }
        form = BookForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('author', form.errors)
        self.assertIn('isbn', form.errors)
        self.assertIn('description', form.errors)
        self.assertIn('available_copies', form.errors)

    def test_featured_image_field(self):
        """
        Test that the featured_image field can be included in the form data.
        Obs: Image is optional as some books maybe have no original book cover
        """
        form_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'isbn': '1234567890123',
            'description': 'A test book description.',
            'available_copies': 5,
            'featured_image': None
        }
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())
