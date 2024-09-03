from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().prefetch_related('books')
    serializer_class = AuthorSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains=name_filter)
        return queryset
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all() # Fetch book 
    serializer_class = BookSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        author_name = self.request.query_params.get('author', None)
        if author_name is not None:
            queryset = queryset.filter(author__name__icontains(author_name)) # type: ignore
        return queryset
