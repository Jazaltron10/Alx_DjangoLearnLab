from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Import the Book model
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required  # Import login_required to restrict access to authenticated users only
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

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

# User registration view
class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

# Use Django's built-in LoginView
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    authentication_form = AuthenticationForm

# Use Django's built-in LogoutView
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

@login_required # Decorator to ensure that only logged-in users can access this view
def profile_view(request):
    """
    View to display the user's profile after login.
    This view is only accessible to logged-in users, enforced by the @login_required decorator.
    Renders a template that shows a welcome message to the user and provides a logout button.
    """
    return render(request, 'relationship_app/profile.html', {'user': request.user})  # Pass the current user to the template and render it

# Helper function to check if the user has a specific role
def check_role(user, role):
    return user.is_authenticated and user.userprofile.role == role

# Admin view
@login_required
@user_passes_test(lambda user: user.userprofile.role == 'Admin', login_url='home')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@login_required
@user_passes_test(lambda user: user.userprofile.role == 'Librarian', login_url='home')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@login_required
@user_passes_test(lambda user: user.userprofile.role == 'Member', login_url='home')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')