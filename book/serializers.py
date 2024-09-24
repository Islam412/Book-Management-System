from rest_framework import serializers
from .models import Book 


'''
status_books = [
    ('available', 'available'),
    ('rented', 'rented'),
    ('sold', 'sold'),
]

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    author = serializers.CharField(max_length=200, blank=True)
    photo_book = serializers.ImageField(upload_to='photos_books', null='True', blank=True)
    photo_author = serializers.ImageField(upload_to='photos_authors', null=True, blank=True)
    pages = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    descripition = serializers.TextField(null=True, blank=True)
    created_at = serializers.DateTimeField(auto_now_add=True)
    active = serializers.BooleanField(default=True)
    status = serializers.CharField(max_length=50, choices=status_books, null=True, blank=True)


    def create(self, validated_data):
        """
        Create and return a new `Book` instance, given the validated data.
        """
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Book` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.photo_book = validated_data.get('photo_book', instance.photo_book)
        instance.photo_author = validated_data.get('photo_author', instance.photo_author)
        instance.pages = validated_data.get('pages', instance.pages)
        instance.price = validated_data.get('price', instance.price)
        instance.descripition = validated_data.get('descripition', instance.descripition)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.active = validated_data.get('active', instance.active)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
'''

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['active']