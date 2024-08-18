from django.urls import path
from .views import list_books, LibraryDetailView
from .views import UserRegisterView, UserLoginView, UserLogoutView
from . import views

urlpatterns = [
    # Route for the function-based view to list all books
    path('books/', list_books, name='list_books'),
    
    # Route for the class-based view to display library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Routes for user authentication
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    
    # Example of a profile page
    path('profile/', views.profile_view, name='profile'),
]
