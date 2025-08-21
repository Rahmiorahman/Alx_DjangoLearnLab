# Update Operation\n\n**Command**:\n```python\nfrom bookshelf.models import Book\nbook = Book.objects.get(title="1984")\nbook.title = "Nineteen Eighty-Four"\nbook.save()\nprint(book.title)\n```\n\n**Expected Output**:\n```\nNineteen Eighty-Four\n```\n# Confirms the title of the book has been updated.
# Update Operation

**Command**:
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)