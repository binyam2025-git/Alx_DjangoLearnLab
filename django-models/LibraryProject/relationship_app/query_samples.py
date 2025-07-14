import os
import django

# Configure Django settings (only needed when running script outside manage.py shell)
# This is important if you run this script directly, but not strictly needed inside `manage.py shell`
# However, it's good practice for standalone scripts.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    print("--- Setting up Sample Data ---")
    # Clean up existing data to ensure fresh start (optional, but good for testing)
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create Authors
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="Jane Austen")
    author3 = Author.objects.create(name="J.K. Rowling")
    print(f"Created Authors: {author1.name}, {author2.name}, {author3.name}")

    # Create Books
    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="Pride and Prejudice", author=author2)
    book4 = Book.objects.create(title="Sense and Sensibility", author=author2)
    book5 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author3)
    print(f"Created Books: {book1.title}, {book2.title}, {book3.title}, {book4.title}, {book5.title}")


    # Create Libraries
    library1 = Library.objects.create(name="Central City Library")
    library2 = Library.objects.create(name="University Library")
    print(f"Created Libraries: {library1.name}, {library2.name}")

    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book3, book5)
    library2.books.add(book2, book4, book5) # Book5 is in both libraries
    print("Books added to Libraries.")

    # Create Librarians
    librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)
    librarian2 = Librarian.objects.create(name="Bob Williams", library=library2)
    print(f"Created Librarians: {librarian1.name}, {librarian2.name}")


    print("\n--- Performing Queries ---")

    # Query all books by a specific author.
    print("\nQuery all books by George Orwell:")
    george_orwell_books = Book.objects.filter(author__name="George Orwell")
    for book in george_orwell_books:
        print(f"- {book.title}")

    # List all books in a library.
    print("\nList all books in Central City Library:")
    central_library = Library.objects.get(name="Central City Library")
    for book in central_library.books.all():
        print(f"- {book.title}")

    # Retrieve the librarian for a library.
    print("\nRetrieve the librarian for University Library:")
    university_library = Library.objects.get(name="University Library")
    librarian = Librarian.objects.get(library=university_library)
    print(f"- Librarian for University Library: {librarian.name}")

if __name__ == '__main__':
    run_queries()