# Update Book
python manage.py shell
>>> from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> book.title = "Updated Title"
>>> book.save()
