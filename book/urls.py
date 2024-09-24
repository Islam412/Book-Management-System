from django.urls import path
# from .views import book, add_book, edit_book, delete_book, book_details

app_name = 'book'

'''
# urls off function based view
urlpatterns = [
    path('', book, name='book'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:pk>/', edit_book, name='edit_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),
    path('<int:pk>/', book_details, name='book_details'),
]
'''

# urls off class based view
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView, BookDetailView ,book_list


urlpatterns = [
    path('', BookListView.as_view(), name='book'),
    path('add/', BookCreateView.as_view(), name='add_book'),
    path('edit/<int:pk>/', BookUpdateView.as_view(), name='edit_book'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete_book'),
    path('details/<int:pk>/', BookDetailView.as_view(), name='book_details'),
    
    # api vith functions view
    path('api/list/', book_list, name='book_list'),
]

