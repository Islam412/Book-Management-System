from django.test import TestCase
from django.urls import reverse
from .models import Book
from userauths.models import User

class BookModelTest(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
        # Create test data for a book
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            pages=100,
            price=10.50,
            status="available"
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.pages, 100)
        self.assertEqual(self.book.price, 10.50)
        self.assertEqual(self.book.status, "available")

    def test_book_str(self):
        self.assertEqual(str(self.book), "Test Book")


class BookViewsTest(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')  # Login user
        
        # Create a book for testing views
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            pages=100,
            price=10.50,
            status="available"
        )

    def test_book_list_view(self):
        response = self.client.get(reverse('book:book'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")
        self.assertTemplateUsed(response, 'book/home.html')

    def test_book_detail_view(self):
        response = self.client.get(reverse('book:book_details', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")
        self.assertTemplateUsed(response, 'book/book_detail.html')

    def test_book_create_view(self):
        response = self.client.post(reverse('book:add_book'), {
            'title': 'New Book',
            'author': 'New Author',
            'pages': 120,
            'price': 15.00,
            'status': 'available'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful creation
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_book_update_view(self):
        response = self.client.post(reverse('book:edit_book', args=[self.book.id]), {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'pages': 150,
            'price': 20.00,
            'status': 'rented'
        })
        self.assertEqual(response.status_code, 302)
        self.book.refresh_from_db()  # Reload the book from the database
        self.assertEqual(self.book.title, 'Updated Book')
        self.assertEqual(self.book.status, 'rented')

    def test_book_delete_view(self):
        response = self.client.post(reverse('book:delete_book', args=[self.book.id]), {})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
