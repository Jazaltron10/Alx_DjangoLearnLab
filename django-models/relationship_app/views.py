from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Import the Book model

# Define the function-based view to list all books
def list_books(request):
    # Query all books from the database
    books = Book.objects.all()

    # Render the list_books.html template, passing the list of books to the template
    return render(request, 'relationship_app/list_books.html', {'books': books})



# Define the class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library  # Specify the model to use for this view
    template_name = 'relationship_app/library_detail.html'  # Specify the template to render

    context_object_name = 'library'