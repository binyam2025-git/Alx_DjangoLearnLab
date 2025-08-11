# blog/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment, Tag # Import the Comment model

class CustomUserCreationForm(UserCreationForm):
    # ... (Your existing code) ...
    class Meta:
        model = User
        fields = ("username", "email")
    pass

class UserUpdateForm(forms.ModelForm):
    # ... (Your existing code) ...
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
    pass

class PostForm(forms.ModelForm):
    # ... (Your existing code) ...
    tags = forms.CharField(max_length=250, required=False, help_text="Enter tags separated by commas.")
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
    pass 