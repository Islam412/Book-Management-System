from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Book
from .forms import BookForm

@login_required
def book(request):
    query = request.GET.get('search', '')
    books = Book.objects.filter(
        title__icontains=query
    ) | Book.objects.filter(
        author__icontains=query
    )
    context = {
        'books': books,
        'query': query
    }
    return render(request, 'book/home.html', context)

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book:book')
    else:
        form = BookForm()
    return render(request, 'book/add_book.html', {'form': form})

@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book:book')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/edit_book.html', {'form': form})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book:book')
    return render(request, 'book/delete_book.html', {'book': book})
