# Delete Book Instance

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four") # Retrieve the book using its updated title
book.delete() # Delete the book instance
Book.objects.all() # Confirm deletion by checking all books

