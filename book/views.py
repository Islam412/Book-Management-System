from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Book
from .forms import BookForm

@login_required
def home(request):
    return render(request, 'book/home.html')


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book:book_list')
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
            return redirect('book:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/edit_book.html', {'form': form})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book:book_list')
    return render(request, 'book/delete_book.html', {'book': book})