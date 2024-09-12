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