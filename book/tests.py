
from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookModelTest(TestCase):

    def setUp(self):
        # Create test data for a book
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            pages=100,
            price=10.50,
            status="available"
        )

    def test_book_creation(self):
        # Ensure the book was created correctly
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.pages, 100)
        self.assertEqual(self.book.price, 10.50)
        self.assertEqual(self.book.status, "available")

    def test_book_str(self):
        # Ensure the __str__ method returns the correct title
        self.assertEqual(str(self.book), "Test Book")


class BookViewsTest(TestCase):

    def setUp(self):
        # Create a book for testing views
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            pages=100,
            price=10.50,
            status="available"
        )

    def test_book_list_view(self):
        # Test the book list view response and content
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")
        self.assertTemplateUsed(response, 'book/home.html')

    def test_book_detail_view(self):
        # Test the book detail view response and content
        response = self.client.get(reverse('book_details', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")
        self.assertTemplateUsed(response, 'book/book_detail.html')

    def test_book_create_view(self):
        # Test creating a new book using the create view
        response = self.client.post(reverse('add_book'), {
            'title': 'New Book',
            'author': 'New Author',
            'pages': 120,
            'price': 15.00,
            'status': 'available'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful creation
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_book_update_view(self):
        # Test updating a book's information
        response = self.client.post(reverse('edit_book', args=[self.book.id]), {
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
        # Test deleting a book
        response = self.client.post(reverse('delete_book', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())


