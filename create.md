# Create Operation\n\n**Command**:\n```python\nfrom bookshelf.models import Book\nbook = Book(title="1984", author="George Orwell", publication_year=1949)\nbook.save()\n```\n\n**Expected Output**:\n```\n# No output in the shell, but the Book instance is successfully created and saved to the database.\n```
# Create Operation

**Command**:
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()