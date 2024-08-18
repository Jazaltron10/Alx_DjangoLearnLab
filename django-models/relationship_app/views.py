from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView

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

# User registration view
class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request.POST or None)  # Explicitly using UserCreationForm()

# Use Django's built-in LoginView
class LoginView(LoginView):
    template_name = 'relationship_app/login.html'
    authentication_form = AuthenticationForm

# Use Django's built-in LogoutView
class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
