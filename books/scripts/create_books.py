# books/scripts/create_books.py

import os
import django
from books.models import Book

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_project.settings')
django.setup()

# List of book data
books_data = [
    {
        'title': 'The Enchanted Forest',
        'author': 'Lila Winters',
        'description': (
            'A magical journey through an enchanted forest where mythical '
            'creatures and hidden secrets await.'
        ),
        'isbn': '9781234567890',
        'available_copies': 5
    },
    {
        'title': 'The Time Traveler\'s Diary',
        'author': 'Alex Harper',
        'description': (
            'A captivating tale of a time traveler who discovers ancient '
            'civilizations and future societies through an old diary.'
        ),
        'isbn': '9781234567891',
        'available_copies': 3
    },
    {
        'title': 'Mysteries of the Deep',
        'author': 'Sam Rivers',
        'description': (
            'An adventurous exploration into the uncharted depths of the '
            'ocean, revealing lost cities and extraordinary sea life.'
        ),
        'isbn': '9781234567892',
        'available_copies': 4
    },
    {
        'title': 'The Last Alchemist',
        'author': 'Evelyn Sage',
        'description': (
            'A thrilling narrative about the last remaining alchemist who '
            'holds the key to a powerful ancient secret.'
        ),
        'isbn': '9781234567893',
        'available_copies': 6
    },
    {
        'title': 'Dreams of Stardust',
        'author': 'R.J. Moon',
        'description': (
            'A poetic and imaginative story set in a world where dreams '
            'and reality intertwine under a stardust sky.'
        ),
        'isbn': '9781234567894',
        'available_copies': 2
    },
    {
        'title': 'Echoes of the Past',
        'author': 'Clara Weston',
        'description': (
            'A gripping historical novel that unearths long-forgotten '
            'events and the echoes they leave behind in the present day.'
        ),
        'isbn': '9781234567895',
        'available_copies': 7
    },
]

# Create book instances
for book_data in books_data:
    Book.objects.create(**book_data)
