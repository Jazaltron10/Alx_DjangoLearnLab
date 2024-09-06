from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from api.models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Ensure the user exists in the test database or create them
        self.user = User.objects.create_user(
            username='admin_user',
            password='adminpassword'
        )
        # Create a token for this user
        self.token = Token.objects.create(user=self.user)

        # Set up authorization using the token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create an author and a book for testing
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2020,
            author=self.author,
            owner=self.user
        )

        # Set URLs
        # Define the URLs for each of your API views
        self.book_list_url = reverse('book-list')
        self.book_create_url = reverse('book-create')
        self.book_detail_url = reverse('book-detail', args=[1])  # Change the pk as needed
        self.book_update_url = reverse('book-update', args=[1])
        self.book_delete_url = reverse('book-delete', args=[1])


    def test_create_book(self):
        url = self.book_create_url
        data = {
            'title': 'New Book',
            'publication_year': 2021,
            'author': self.author.id,
            'owner': self.user.id
        }
        response = self.client.post(url, data, format='json')
        print(response.data)  # Print response for debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_update_book(self):
        data = {
            'title': 'Updated Book Title',
            'publication_year': 2021,
            'author': self.author.id,
            'owner': self.user.id
        }
        response = self.client.put(self.book_detail_url, data, format='json')
        print(response.data)  # Print response for debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url)
        print(response.data)  # Print response for debugging
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_book_by_author(self):
        response = self.client.get(self.book_list_url, {'author': self.author.id})
        print(response.data)  # Print response for debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_book_by_title(self):
        response = self.client.get(self.book_list_url, {'search': 'Test'})
        print(response.data)  # Print response for debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_book_by_publication_year(self):
        response = self.client.get(self.book_list_url, {'ordering': 'publication_year'})
        print(response.data)  # Print response for debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_unauthorized_create_book(self):
        self.client.logout()  # Simulate an unauthenticated user
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post(self.book_create_url, data, format='json')
        print(response.data)  # Print response for debugging
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
