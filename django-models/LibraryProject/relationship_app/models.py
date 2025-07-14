from django.db import models

# Create your models here.
# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book Model (ForeignKey to Author)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # ForeignKey relationship

    def __str__(self):
        return f"{self.title} by {self.author.name}"

# Library Model (ManyToManyField to Book)
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book) # ManyToManyField relationship

    def __str__(self):
        return self.name

# Librarian Model (OneToOneField to Library)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE) # OneToOneField relationship

    def __str__(self):
        return f"{self.name} (Librarian at {self.library.name})"
