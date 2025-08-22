# CRUD Operations on Book Model

This document shows how to perform **Create, Retrieve, Update, and Delete** operations on the `Book` model in Django using the interactive shell.

---

## 1. Create a Book

### Command:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

Output:
<Book: 1984 by George Orwell (1949)>


Retrieve Operation
Command:
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

Output:
1984 George Orwell 1949

Update Operation
Command:
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

Output:
Nineteen Eighty-Four

Delete Operation
Command:
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())

Output:
<QuerySet []>
