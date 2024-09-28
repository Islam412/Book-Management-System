from django.urls import path

# urls off function off views
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
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView, BookDetailView ,book_list, book_detail , BookList, BookDetail, BookCreateAPIView, BookListAPIViews, BookUpdateAPIView, BookDeleteAPIView


urlpatterns = [
    path('', BookListView.as_view(), name='book'),
    path('add/', BookCreateView.as_view(), name='add_book'),
    path('edit/<int:pk>/', BookUpdateView.as_view(), name='edit_book'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete_book'),
    path('details/<int:pk>/', BookDetailView.as_view(), name='book_details'),
    
    # api vith functions view
    path('api/list/', book_list, name='book_list'),
    path('api/detail/<int:pk>/', book_detail, name='book_detail'),
    
    # api with class based view
    path('api/book/', BookList.as_view(), name='book_list_views'),
    path('api/book/<int:pk>/', BookDetail.as_view(), name='book_detail_views'),
    
    # api with generic class based view
    path('api/book/generic', BookCreateAPIView.as_view(), name='book_create_generic'),
    path('api/book/generic/list', BookListAPIViews.as_view(), name='book_list_generic'),
    path('api/book/generic/update/<pk>/', BookUpdateAPIView.as_view(), name='book_update_generic'),
    path('api/book/generic/delete/<pk>/', BookDeleteAPIView.as_view(), name='book_delete_generic'),
]

