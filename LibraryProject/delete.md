
---

### 📒 `LibraryProject/delete.md`
```markdown
# Delete a Book

### Command:
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()
Book.objects.all()

[]
