# api/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        """Set up an author and a user for testing."""
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(title="1984", publication_year=1949, author=self.author)
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Define URLs for easy access
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    def test_list_books_unauthenticated(self):
        """Ensure all users can retrieve the list of books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated users cannot create books."""
        data = {'title': 'Brave New World', 'publication_year': 1932, 'author': self.author.pk}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 1)

    def test_create_book_authenticated(self):
        """Ensure authenticated users can create books."""
        self.client.force_authenticate(user=self.user)
        data = {'title': 'The Great Gatsby', 'publication_year': 1925, 'author': self.author.pk}
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book_authenticated(self):
        """Ensure authenticated users can update a book."""
        self.client.force_authenticate(user=self.user)
        updated_title = "Nineteen Eighty-Four"
        data = {'title': updated_title, 'publication_year': 1949, 'author': self.author.pk}
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, updated_title)

    def test_delete_book_authenticated(self):
        """Ensure authenticated users can delete a book."""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_search_books(self):
        """Ensure search functionality works correctly."""
        Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author)
        response = self.client.get(self.list_url + '?search=Animal')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Animal Farm')

    def test_order_books(self):
        """Ensure ordering functionality works correctly."""
        book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author)
        response = self.client.get(self.list_url + '?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        # Check if the most recent book is first
        self.assertEqual(response.data[0]['title'], self.book.title)