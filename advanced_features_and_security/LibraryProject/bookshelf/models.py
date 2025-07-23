# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\bookshelf\models.py

from django.db import models
from relationship_app.models import Author # Assuming Book links to Author

class Book(models.Model):
    # *** VERY IMPORTANT: Note down the exact spelling and case of these fields ***
    #title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='bookshelf_books')
    #publication_date = models.DateField(null=True, blank=True)
   # isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
   # genre = models.CharField(max_length=100, null=True, blank=True)
    #is_available = models.BooleanField(default=True)
    # ... any other fields you have defined for Book ...

    def __str__(self):
        return self.title