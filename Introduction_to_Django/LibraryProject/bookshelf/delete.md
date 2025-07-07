\# Delete Book Instance



\## Command:

```python

from bookshelf.models import Book

book\_to\_delete = Book.objects.get(title="Nineteen Eighty-Four")

book\_to\_delete.delete()

Book.objects.all()

