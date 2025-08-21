# Create Book
python manage.py shell
>>> from bookshelf.models import Book
>>> Book.objects.create(title="Test Book", author="John Doe", published_date="2025-08-21")

