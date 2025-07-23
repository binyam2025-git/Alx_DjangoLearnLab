# C:\Users\user\Alx_DjangoLearnLab\django-models\LibraryProject\relationship_app\forms.py

from django import forms
from .models import Book, Author, Library # Import any models your forms will use

class MyForm(forms.Form):
    """
    A simple form for demonstration of CSRF protection.
    """
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(widget=forms.Textarea, required=False)

class BookForm(forms.ModelForm):
    """
    Form to create or update a Book instance.
    """
    class Meta:
        model = Book
        # Ensure 'author' and 'library' are fields if they are FKs in your Book model.
        # Adjust fields based on your actual Book model definition.
        # This 'library' field should now exist in relationship_app.models.Book
        fields = ['title', 'author', 'library']
        # You might want to add widgets for better UI
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Book Title'}),
        }

# If you have forms for other models like Author, Librarian, etc., add them here as well
# Example:
# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = '__all__'

# class LibrarianForm(forms.ModelForm):
#     class Meta:
#         model = Librarian
#         fields = '__all__'