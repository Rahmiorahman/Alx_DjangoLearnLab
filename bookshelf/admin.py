from django.contrib import admin

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # show these fields in list view
    search_fields = ('title', 'author')                     # enable search by title/author
    list_filter = ('publication_year',)                     # filter by year

# Register the model with custom admin
admin.site.register(Book, BookAdmin)
