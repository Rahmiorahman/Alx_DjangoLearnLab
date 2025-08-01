import os
import sys
import django

# Add the project root to the Python path (this is the folder where manage.py is)
sys.path.append(os.path.dirname(os.path.abspath(__file__)).rsplit('/', 1)[0])

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Setup Django
django.setup()

# Step 2: Import your models
from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"\n📚 Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"\n❌ Author '{author_name}' not found.")

# 2️⃣ List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\n🏛 Books in '{library.name}':")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"\n❌ Library '{library_name}' not found.")

# 3️⃣ Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"\n👤 Librarian for '{library.name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"\n❌ Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"\n⚠️ No librarian assigned to '{library_name}'.")

# Run queries with sample inputs
if __name__ == '__main__':
    query_books_by_author("Jane Austen")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
