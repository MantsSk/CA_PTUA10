from django.urls import path
from library.views import index, authors, author, BookListView, BookDetailView, search, MyBookListView

urlpatterns = [
    path('', index, name='homepage'),
    path('authors/', authors, name='authors'),
    path('authors/<int:author_id>', author, name='author'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('search/', search, name='search'),
    path('my-books/', MyBookListView.as_view(), name='my-books')
]