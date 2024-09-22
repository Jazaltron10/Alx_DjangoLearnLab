from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from .views import follow_user, unfollow_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Route for user registration
    path('login/', LoginView.as_view(), name='login'),  # Route for user login
    path('profile/', ProfileView.as_view(), name='profile'),  # Route for profile management
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
]