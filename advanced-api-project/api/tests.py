from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

# Create your tests here.
class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='Author A')
        self.book = Book.objects.create(title='Book One', author=self.author, publication_year=2020)
        self.create_url = reverse('book-create')
        self.list_url = reverse('book-list')

    def test_unauthenticated_user_can_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_create_book(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            'title': 'New Book',
            'author': self.author.id,
            'publication_year': 2024
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_authenticated_user_can_update_book(self):
        self.client.login(username='testuser', password='testpass')
        update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        data = {
            'title': 'Updated Title',
            'author': self.author.id,
            'publication_year': 2023
        }
        response = self.client.put(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_authenticated_user_can_delete_book(self):
        self.client.login(username='testuser', password='testpass')
        delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + f'?author={self.author.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url + '?search=Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        Book.objects.create(title='Book Two', author=self.author, publication_year=2021)
        response = self.client.get(self.list_url + '?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data[0]['publication_year'], response.data[1]['publication_year'])

    def test_unauthenticated_user_cannot_create_book(self):
        data = {
            'title': 'Unauthorized Book',
            'author': self.author.id,
            'publication_year': 2025
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
