from django.urls import path 
from .views import BookListCreateAPIView

urlpatterns = [
    path("", BookListCreateAPIView.as_view(), name="home"),
    path("api/books", BookListCreateAPIView.as_view(), name="book_list_create"),
]