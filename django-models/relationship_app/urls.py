from django.urls import path
from .views import list_books, LibraryDetailView, LoginView,LogoutView
from . import views

urlpatterns = [
    # Route for the function-based view to list all books
    path('books/', list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
    
    # Route for the class-based view to display library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Routes for user authentication
    path('register/', views.register.as_view(), name='register'),  # User registration view
    
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # User login view with template
    
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # User logout view with template
    
    # Custom role-based views with updated paths
    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    path('member-dashboard/', views.member_view, name='member_view'),
]
