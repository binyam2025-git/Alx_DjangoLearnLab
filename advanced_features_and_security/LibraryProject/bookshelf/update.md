\# Update Book Instance



\## Command:

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984") # Retrieve the book using its current title
book.title = "Nineteen Eighty-Four" # Update the title
book.save() # Save the changes
print(book.title) # Print the updated title to show the change

