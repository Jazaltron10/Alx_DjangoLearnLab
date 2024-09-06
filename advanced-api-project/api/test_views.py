from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    
    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        
        # Create test data
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2021)
        self.book3 = Book.objects.create(title="Another Book", author="Author A", publication_year=2019)
        
        self.book_url = reverse('book-list')  # Assuming 'book-list' is the name of your Book viewset URL
    
    def test_create_book(self):
        # Test creating a book
        data = {
            "title": "New Book",
            "author": "Author C",
            "publication_year": 2022
        }
        response = self.client.post(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, "New Book")

    def test_update_book(self):
        # Test updating a book
        data = {
            "title": "Updated Title",
            "author": self.book1.author,
            "publication_year": self.book1.publication_year
        }
        url = reverse('book-detail', args=[self.book1.id])  # Assuming 'book-detail' is the name of your Book detail URL
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        # Test deleting a book
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_filter_books_by_author(self):
        # Test filtering books by author
        response = self.client.get(self.book_url, {'author': 'Author A'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two books by 'Author A'

    def test_search_books_by_title_and_author(self):
        # Test searching books by title and author
        response = self.client.get(self.book_url, {'search': 'Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Two books with 'Book' in the title or author

        response = self.client.get(self.book_url, {'search': 'Author B'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # One book by 'Author B'

    def test_order_books_by_publication_year(self):
        # Test ordering books by publication year
        response = self.client.get(self.book_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2019)  # The earliest year

        response = self.client.get(self.book_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2021)  # The latest year
