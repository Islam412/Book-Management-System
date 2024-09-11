from django.contrib import admin
from .models import Book

# Register your models here.

class BookCustomAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'active', 'status']
    list_filter = ['active','status']
    search_fields = ['title','author','descripition']
    

admin.site.register(Book, BookCustomAdmin)