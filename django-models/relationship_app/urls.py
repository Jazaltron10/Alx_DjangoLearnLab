from django.urls import path
from .views import list_books, LibraryDetailView, LoginView,LogoutView
from . import views

urlpatterns = [
    # Route for the function-based view to list all books
    path('books/', list_books, name='list_books'),
    
    # Route for the class-based view to display library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Routes for user authentication
    path('register/', views.register.as_view(), name='register'),  # User registration view
    
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # User login view with template
    
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # User logout view with template
]
