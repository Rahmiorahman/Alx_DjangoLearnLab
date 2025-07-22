from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in list view
    list_filter = ('publication_year',)  # Filter sidebar by publication year
    search_fields = ('title', 'author')  # Enable search by title and author
# Register your models here.
