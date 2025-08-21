
## Create Operation
**Command**:
```python
CRUD Operations for Book Model
Create Operation
Command:
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

Output:
# No output in the shell, but the Book instance is successfully created and saved.

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
