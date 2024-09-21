# accounts/urls.py
from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Route for user registration
    path('login/', LoginView.as_view(), name='login'),  # Route for user login
]
