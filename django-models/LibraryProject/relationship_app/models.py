# relationship_app/models.py

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField(null=True, blank=True) # <--- Add this line

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    # ManyToManyField: A library can have many books, and a book can be in many libraries.
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # OneToOneField: A librarian is responsible for one specific library, and a library has one librarian.
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name
