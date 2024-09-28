from django.db import models

# Create your models here.

status_books = [
    ('available', 'available'),
    ('rented', 'rented'),
    ('sold', 'sold'),
]

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True)
    photo_book = models.ImageField(upload_to='photos_books', null='True', blank=True, default='book.jpg')
    photo_author = models.ImageField(upload_to='photos_authors', null=True, blank=True)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    descripition = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_books, null=True, blank=True)

    def __str__(self):
        return self.title