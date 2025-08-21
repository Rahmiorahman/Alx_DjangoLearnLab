# Delete Operation\n\n**Command**:\n```python\nfrom bookshelf.models import Book\nbook = Book.objects.get(title="Nineteen Eighty-Four")\nbook.delete()\nprint(Book.objects.all())\n```\n\n**Expected Output**:\n```\n<QuerySet []>\n```\n# Confirms the book has been deleted, as the QuerySet is empty.
# Delete Operation

**Command**:
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())