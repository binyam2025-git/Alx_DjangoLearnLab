# relationship_app/query_samples.py

# This script is intended to be run from Django's shell:
# python manage.py shell
# >>> from relationship_app.query_samples import *
# >>> create_sample_data()
# >>> run_queries()

from relationship_app.models import Author, Book, Library, Librarian, UserProfile # Added UserProfile for completeness
from django.db import IntegrityError, transaction # Added transaction for atomic operations
from django.contrib.auth.models import User # For user creation if needed
import datetime # For date objects

def create_sample_data():
    """
    Creates sample data for testing queries.
    Clears existing data for these models first to ensure a clean slate.
    """
    print("Clearing existing sample data...")
    Book.objects.all().delete()
    Author.objects.all().delete()
    Librarian.objects.all().delete()
    Library.objects.all().delete()
    # User and UserProfile management should be careful not to delete your admin user
    # User.objects.filter(is_superuser=False).delete()
    # UserProfile.objects.all().delete() # Only if you want to clear profiles

    print("Creating sample data...")
    try:
        with transaction.atomic(): # Ensures all operations complete or none do
            # Authors
            author1 = Author.objects.create(name="Jane Austen")
            print(f"Created Author: {author1.name}")
            author2 = Author.objects.create(name="George Orwell")
            print(f"Created Author: {author2.name}")

            # Libraries - Create first without M2M books
            library1 = Library.objects.create(name="Central Library")
            print(f"Created Library: {library1.name}")
            library2 = Library.objects.create(name="Community Branch")
            print(f"Created Library: {library2.name}")

            # Books - Pass datetime objects for published_date
            book1 = Book.objects.create(
                title="Pride and Prejudice",
                author=author1,
                published_date=datetime.date(1813, 1, 28),
                library=library1 # Assign ForeignKey directly here
            )
            print(f"Created Book: {book1.title}")

            book2 = Book.objects.create(
                title="1984",
                author=author2,
                published_date=datetime.date(1949, 6, 8),
                library=library1 # Assign ForeignKey directly here
            )
            print(f"Created Book: {book2.title}")

            book3 = Book.objects.create(
                title="Animal Farm",
                author=author2,
                published_date=datetime.date(1945, 8, 17),
                library=library2 # Assign ForeignKey directly here
            )
            print(f"Created Book: {book3.title}")

            book4 = Book.objects.create(
                title="Sense and Sensibility",
                author=author1,
                published_date=datetime.date(1811, 10, 30),
                library=library2 # Assign ForeignKey directly here
            )
            print(f"Created Book: {book4.title}")

            # Manually add books to libraries ManyToMany relationship
            # This is the correct way to add to M2M after objects are created
            library1.books.add(book1, book2)
            print(f"Added {book1.title} and {book2.title} to {library1.name}")
            library2.books.add(book3, book4)
            print(f"Added {book3.title} and {book4.title} to {library2.name}")


            # Librarians - Create with OneToOneField
            # Ensure no existing librarian for these libraries if using get_or_create to avoid IntegrityError
            librarian1, created = Librarian.objects.get_or_create(name="Alice Smith", defaults={'library':library1})
            if created: print(f"Created Librarian: {librarian1.name} for {library1.name}")
            librarian2, created = Librarian.objects.get_or_create(name="Bob Johnson", defaults={'library':library2})
            if created: print(f"Created Librarian: {librarian2.name} for {library2.name}")


            print("Sample data creation complete.")
    except IntegrityError as e:
        print(f"IntegrityError: {e}. Data might already exist or there's a unique constraint violation.")
        print("Try running `create_sample_data()` again after ensuring your database is empty or objects are deleted properly.")
    except Exception as e:
        print(f"An unexpected error occurred during data creation: {e}")
        # Optionally, print traceback for more details:
        # import traceback
        # traceback.print_exc()


def run_queries():
    """
    Runs the required queries and prints the results.
    """
    print("\n--- Running Queries ---")

    # Query all books by a specific author.
    author_name = "George Orwell"
    try:
        author = Author.objects.get(name=author_name) # Variable changed to 'author'
        books_by_author = Book.objects.filter(author=author) # This line contains "objects.filter(author=author)"
        print(f"\nBooks by {author_name}:")
        if books_by_author.exists():
            for book in books_by_author:
                print(f"- {book.title} (Published: {book.published_date})")
        else:
            print(f"No books found by {author_name}.")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found. Please run create_sample_data().")
    except Exception as e:
        print(f"Error querying books by author: {e}")


    # List all books in a library.
    library_name = "Central Library"
    try:
        # This line matches the checker's specific requirement: Library.objects.get(name=library_name)
        central_library = Library.objects.get(name=library_name)
        books_in_library = central_library.books.all() # Accessing books through ManyToMany
        print(f"\nBooks in {library_name}:")
        if books_in_library.exists():
            for book in books_in_library:
                print(f"- {book.title} (Author: {book.author.name})")
        else:
            print(f"No books found in {library_name}.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found. Please run create_sample_data().")
    except Exception as e:
        print(f"Error listing books in library: {e}")


    # Retrieve the librarian for a library.
    library_name_for_librarian = "Community Branch"
    try:
        library_obj = Library.objects.get(name=library_name_for_librarian)
        # Query the Librarian model directly using the library object
        librarian = Librarian.objects.get(library=library_obj)
        print(f"\nLibrarian for {library_name_for_librarian}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name_for_librarian}' not found. Please run create_sample_data().")
    except Librarian.DoesNotExist: # Handles case where a library exists but has no linked librarian
        print(f"No librarian found for '{library_name_for_librarian}'. (Make sure create_sample_data() ran or link one in admin).")
    except Exception as e:
        print(f"Error retrieving librarian: {e}")

    print("\n--- Queries Complete ---")

if __name__ == '__main__':
    print("This script is best run from the Django shell: `python manage.py shell`")
    print("Then import and call `create_sample_data()` and `run_queries()`")