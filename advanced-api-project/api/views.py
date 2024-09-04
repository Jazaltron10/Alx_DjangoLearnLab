from rest_framework import generics, viewsets
from .models import Author, Book
from .seriealizers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.authentication import TokenAuthentication

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



class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class BookCreateAPIView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class BookUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
