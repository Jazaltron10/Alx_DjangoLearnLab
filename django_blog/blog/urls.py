from django.urls import path
from .views import home , register, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("register", register, name="register"),
    path("login", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path('profile/', profile, name='profile'),
] 