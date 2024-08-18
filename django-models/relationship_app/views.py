from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Import the Book model

# Define the function-based view to list all books
def list_books(request):
    # Query all books from the database
    books = Book.objects.all()

    # Render the list_books.html template, passing the list of books to the template
    return render(request, 'list_books.html', {'books': books})



# Define the class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library  # Specify the model to use for this view
    template_name = 'library_detail.html'  # Specify the template to render

    # Override the context data to include related books
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Get all books related to the library
        return context
