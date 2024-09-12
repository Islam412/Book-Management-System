from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Book
from .forms import BookForm

@login_required
def home(request):
    return render(request, 'book/home.html')

class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/create_book.html'
    success_url = reverse_lazy('book:book-list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/update_book.html'
    success_url = reverse_lazy('book:book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/delete_book.html'
    success_url = reverse_lazy('book:book-list')
