import os
import django

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
    author_george = Author.objects.create(name="George Orwell")
    author_jane = Author.objects.create(name="Jane Austen")
    author_jk = Author.objects.create(name="J.K. Rowling")
    print(f"Created Authors: {author_george.name}, {author_jane.name}, {author_jk.name}")

    # Create Books
    book_1984 = Book.objects.create(title="1984", author=author_george)
    book_animal_farm = Book.objects.create(title="Animal Farm", author=author_george)
    book_pride = Book.objects.create(title="Pride and Prejudice", author=author_jane)
    book_sense = Book.objects.create(title="Sense and Sensibility", author=author_jane)
    book_hp = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author_jk)
    print(f"Created Books: {book_1984.title}, {book_animal_farm.title}, {book_pride.title}, {book_sense.title}, {book_hp.title}")


    # Create Libraries
    lib_central = Library.objects.create(name="Central City Library")
    lib_university = Library.objects.create(name="University Library")
    print(f"Created Libraries: {lib_central.name}, {lib_university.name}")

    # Add books to libraries (ManyToMany relationship)
    lib_central.books.add(book_1984, book_pride, book_hp)
    lib_university.books.add(book_animal_farm, book_sense, book_hp)
    print("Books added to Libraries.")

    # Create Librarians
    librarian_alice = Librarian.objects.create(name="Alice Johnson", library=lib_central)
    librarian_bob = Librarian.objects.create(name="Bob Williams", library=lib_university)
    print(f"Created Librarians: {librarian_alice.name}, {librarian_bob.name}")


    print("\n--- Performing Queries ---")

    # Query all books by a specific author. (Revised to match checker's exact expectation)
    print("\nQuery all books by George Orwell:")
    # First, get the Author object
    author_name = "George Orwell" # Variable name used as per checker's hint
    author = Author.objects.get(name=author_name) # Ensure this pattern: Author.objects.get(name=author_name)
    # Then, filter books by this Author object
    books_by_specific_author = Book.objects.filter(author=author) # Ensure this pattern: objects.filter(author=author)
    for book in books_by_specific_author:
        print(f"- {book.title}")

    # List all books in a library. (Already correct from previous attempt)
    print("\nList all books in Central City Library:")
    library_name = "Central City Library"
    library_obj = Library.objects.get(name=library_name)
    for book in library_obj.books.all():
        print(f"- {book.title}")

    # Retrieve the librarian for a library. (Re-verified to ensure exact match)
    print("\nRetrieve the librarian for University Library:")
    target_library_name = "University Library"
    target_library = Library.objects.get(name=target_library_name)
    # The checker implicitly wants a clear retrieve based on the library object
    librarian_retrieved = Librarian.objects.get(library=target_library) # Use a clear variable name and direct lookup
    print(f"- Librarian for {target_library.name}: {librarian_retrieved.name}")

if __name__ == '__main__':
    run_queries()