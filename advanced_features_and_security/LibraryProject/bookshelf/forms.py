# C:\Users\user\Alx_DjangoLearnLab\advanced_features_and_security\LibraryProject\bookshelf\forms.py

from django import forms
# Correct import for Book: It should come from relationship_app.models
# We import Author and Library as well, as BookForm needs to display choices for them.
from relationship_app.models import Book, Author, Library


# Form for creating/editing Book objects
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # Ensure these fields exactly match the names in relationship_app/models.py Book model.
        # This list correctly reflects the activated fields in your Book model.
        fields = ['title', 'author', 'library', 'publication_date', 'genre', 'isbn', 'is_available']

        # Optional: Add widgets for better control over form fields (e.g., DateInput for dates)
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }

# If you have other forms in the bookshelf app, add them here.
# For instance, if you still need an 'ExampleForm' as a generic demonstration, keep it.
# Otherwise, remove it if it's not being used.
class ExampleForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    message = forms.CharField(label="Your message", widget=forms.Textarea)