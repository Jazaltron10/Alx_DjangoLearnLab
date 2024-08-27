from django.urls import path 
from .views import BookList

urlpatterns = [
    # path("", BookList.as_view(), name="home"),
    path('books/', BookList.as_view(), name='book-list'),
]



