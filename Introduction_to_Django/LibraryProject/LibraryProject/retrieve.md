from bookshelf.models import Book
Book.objects.all()
Book.objects.get(id=1)
# Expected Output: <Book: 1984 by George Orwell (1949)>

