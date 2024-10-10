from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookViewsTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(title='Test Book', author='Author Name', pages=100)

    def test_book_create_view(self):
        response = self.client.post(reverse('book:create'), {'title': 'New Book', 'author': 'Author Name', 'pages': 150})
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after creation

    def test_book_delete_view(self):
        response = self.client.post(reverse('book:delete', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)

    def test_book_detail_view(self):
        response = self.client.get(reverse('book:detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_book_list_view(self):
        response = self.client.get(reverse('book:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_book_update_view(self):
        response = self.client.post(reverse('book:update', args=[self.book.id]), {'title': 'Updated Title', 'author': 'Updated Author', 'pages': 200})
        self.assertEqual(response.status_code, 302)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')
