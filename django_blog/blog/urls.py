from django.urls import path
from .views import register, profile
from django.contrib.auth import views as auth_views
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    # path("", home, name="home"),
    path('', ListView.as_view(), name='post-list'),
    path('post/<int:pk>/', DetailView.as_view(), name='post-detail'),
    path('post/new/', CreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='post-delete'),
    path("register", register, name="register"),
    path("login", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path('profile/', profile, name='profile'),
] 

