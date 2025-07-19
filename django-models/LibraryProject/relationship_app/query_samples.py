# relationship_app/query_samples.py

# This script is meant to be run from the Django shell.
# To run:
# 1. Start your Django shell: python manage.py shell
# 2. Inside the shell, paste the setup code (import os, django, etc.)
# 3. Then, paste the sample data creation (optional, if you want fresh data)
# 4. Finally, execute this script using: exec(open('relationship_app/query_samples.py').read())

from relationship_app.models import Author, Book, Library, Librarian
from django.db.models import Count # For more advanced queries

# --- Create some sample data first (if you haven't already created it through the admin or another shell session) ---
# You can uncomment and run these lines once in the Django shell to populate data.
# If you run them again, get_or_create will ensure duplicates are not made for existing entries.
print("\n--- Ensuring Sample Data Exists ---")
author1, created1 = Author.objects.get_or_create(name="Jane Doe")
if created1: print(f"Created author: {author1.name}")
author2, created2 = Author.objects.get_or_create(name="John Smith")
if created2: print(f"Created author: {author2.name}")
author3, created3 = Author.objects.get_or_create(name="Emily White")
if created3: print(f"Created author: {author3.name}")

book1, created_b1 = Book.objects.get_or_create(title="The Adventure Begins", author=author1)
if created_b1: print(f"Created book: {book1.title}")
book2, created_b2 = Book.objects.get_or_create(title="Mystery of the Old House", author=author1)
if created_b2: print(f"Created book: {book2.title}")
book3, created_b3 = Book.objects.get_or_create(title="Coding with Django", author=author2)
if created_b3: print(f"Created book: {book3.title}")
book4, created_b4 = Book.objects.get_or_create(title="The Silent Forest", author=author3)
if created_b4: print(f"Created book: {book4.title}")
book5, created_b5 = Book.objects.get_or_create(title="Django Deep Dive", author=author2)
if created_b5: print(f"Created book: {book5.title}")

library1, created_l1 = Library.objects.get_or_create(name="Central Library")
if created_l1: print(f"Created library: {library1.name}")
library2, created_l2 = Library.objects.get_or_create(name="Community Hub")
if created_l2: print(f"Created library: {library2.name}")

# Add books to libraries (ManyToMany relationship) - check if already added
if not library1.books.filter(id=book1.id).exists(): library1.books.add(book1)
if not library1.books.filter(id=book2.id).exists(): library1.books.add(book2)
if not library1.books.filter(id=book3.id).exists(): library1.books.add(book3)
if not library2.books.filter(id=book3.id).exists(): library2.books.add(book3)
if not library2.books.filter(id=book4.id).exists(): library2.books.add(book4)
if not library2.books.filter(id=book5.id).exists(): library2.books.add(book5)
print("Books added to libraries (if not already present).")


librarian1, created_lib1 = Librarian.objects.get_or_create(name="Alice Johnson", library=library1)
if created_lib1: print(f"Created librarian: {librarian1.name} for {librarian1.library.name}")
# For a OneToOne, ensure the library is not already linked. If it is, this might fail or update.
# We use update_or_create to handle cases where library might already be associated.
librarian2, created_lib2 = Librarian.objects.update_or_create(library=library2, defaults={'name': "Bob Williams"})
if created_lib2: print(f"Created librarian: {librarian2.name} for {librarian2.library.name}")
else: print(f"Updated librarian for {library2.name} to {librarian2.name}")


print("\n--- Sample Queries ---")

print("\n--- Query all books by a specific author (ForeignKey) ---")
try:
    jane_doe = Author.objects.get(name="Jane Doe")
    jane_doe_books = jane_doe.books.all() # Using related_name 'books'
    print(f"Books by {jane_doe.name}:")
    for book in jane_doe_books:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print("Author 'Jane Doe' not found. Please create sample data first.")
except Exception as e:
    print(f"An error occurred: {e}")


print("\n--- List all books in a library (ManyToManyField) ---")
try:
    central_library = Library.objects.get(name="Central Library")
    central_library_books = central_library.books.all()
    print(f"Books in {central_library.name}:")
    for book in central_library_books:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print("Library 'Central Library' not found. Please create sample data first.")
except Exception as e:
    print(f"An error occurred: {e}")


print("\n--- Retrieve the librarian for a library (OneToOneField) ---")
try:
    community_hub = Library.objects.get(name="Community Hub")
    # Using related_name 'librarian' to get the librarian from the library
    community_hub_librarian = community_hub.librarian
    print(f"Librarian for {community_hub.name}: {community_hub_librarian.name}")
except Library.DoesNotExist:
    print("Library 'Community Hub' not found. Please create sample data first.")
except Librarian.DoesNotExist:
    print(f"No librarian found for {community_hub.name}. Please create sample data first.")
except Exception as e:
    print(f"An error occurred: {e}")


print("\n--- Reverse Query: Find the library a librarian belongs to (OneToOneField) ---")
try:
    alice_johnson = Librarian.objects.get(name="Alice Johnson")
    alice_library = alice_johnson.library
    print(f"Alice Johnson is the librarian for: {alice_library.name}")
except Librarian.DoesNotExist:
    print("Librarian 'Alice Johnson' not found. Please create sample data first.")
except Exception as e:
    print(f"An error occurred: {e}")


print("\n--- All libraries a book is in (ManyToManyField reverse) ---")
try:
    coding_book = Book.objects.get(title="Coding with Django")
    coding_libraries = coding_book.libraries.all() # Using related_name 'libraries'
    print(f"'{coding_book.title}' is available in these libraries:")
    for library in coding_libraries:
        print(f"- {library.name}")
except Book.DoesNotExist:
    print("Book 'Coding with Django' not found. Please create sample data first.")
except Exception as e:
    print(f"An error occurred: {e}")

# Example of a more complex query (optional)
print("\n--- Count books per author ---")
authors_with_book_count = Author.objects.annotate(num_books=Count('books')).order_by('name')
for author in authors_with_book_count:
    print(f"{author.name}: {author.num_books} books")