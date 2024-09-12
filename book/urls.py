from django.urls import path
from .views import home, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

app_name = 'book'

urlpatterns = [
    path('', home, name='home'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
