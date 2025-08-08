from django.urls import path
from .views import CustomBookListView, CustomBookDetailView, CustomBookCreateView, CustomBookUpdateView, CustomBookDeleteView


urlpatterns = [
    # List all books
    path('books/', CustomBookListView.as_view(), name='book-list'),
    # Create a new book
    path('books/create/', CustomBookCreateView.as_view(), name='book-create'),
    # Get a book by ID (Detail View)
    path('books/<int:id>/', CustomBookDetailView.as_view(), name='book-detail'),
    # Update a book by ID
    path('books/update/', CustomBookUpdateView.as_view(), name='book-update'),
    # Delete a book by ID
    path('books/delete/', CustomBookDeleteView.as_view(), name='book-delete'),
]
