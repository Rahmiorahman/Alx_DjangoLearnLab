
---

### 📕 `LibraryProject/update.md`
```markdown
# Update a Book

### Command:
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Animal Farm"
book.save()
book

<Book: Animal Farm by George Orwell (1949)>
