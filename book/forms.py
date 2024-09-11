from django import forms

from .models import Book


class BookForm(forms.Form):
    models = Book
    fields = '__all__'