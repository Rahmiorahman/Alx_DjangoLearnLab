

### 📙 `LibraryProject/retrieve.md`
```markdown
# Retrieve a Book

### Command:
```python
from bookshelf.models import Book
Book.objects.all()
Book.objects.get(id=1)

<Book: 1984 by George Orwell (1949)>

