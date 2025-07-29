# bookshelf/forms.py
from django import forms
from .models import Book # Assuming you have a Book model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year'] # Use fields from your Book model

    # Custom validation for 'title'
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        if "badword" in title.lower(): # Simple example, you'd use a more robust check
            raise forms.ValidationError("Titles cannot contain 'badword'.")
        return title

    # Custom validation for 'publication_year'
    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        # Using 2025 as the max year, based on your system time
        if not (1000 <= year <= 2025):
            raise forms.ValidationError("Publication year must be between 1000 and 2025.")
        return year

    # General clean method for multiple fields
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        if title and author and title.lower() == author.lower():
            self.add_error(None, "Title and author cannot be the same.") # Non-field error
        return cleaned_data