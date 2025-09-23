# api/views.py
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books / Create new book
class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: Returns all books.
    POST: Creates a new book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: Authenticated users can POST, anyone can GET
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# Retrieve / Update / Delete book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve book by ID.
    PUT/PATCH: Update book (authenticated only).
    DELETE: Remove book (authenticated only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: Authenticated for edit/delete, anyone can view
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
