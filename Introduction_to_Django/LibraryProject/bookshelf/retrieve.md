\# Retrieve Book Instance



\## Command:

```python

from bookshelf.models import Book

retrieved\_book = Book.objects.get(title="1984")

print(retrieved\_book.title)

print(retrieved\_book.author)

print(retrieved\_book.publication\_year)

