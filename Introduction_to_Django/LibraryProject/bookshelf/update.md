\# Update Book Instance



\## Command:

```python

from bookshelf.models import Book

book\_to\_update = Book.objects.get(title="1984") # Or you might need to get by pk if you deleted the previous one

book\_to\_update.title = "Nineteen Eighty-Four"

book\_to\_update.save()

print(book\_to\_update.title)

