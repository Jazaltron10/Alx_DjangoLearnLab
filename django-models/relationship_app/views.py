from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all books related to this library
        context['books'] = Book.objects.filter(library=self.object)
        return context
