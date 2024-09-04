from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, BookListAPIView, BookCreateAPIView, BookDetailAPIView, BookUpdateAPIView, BookDeleteAPIView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('books/list/', BookListAPIView.as_view(), name='book-list'),
    path('books/create/', BookCreateAPIView.as_view(), name='book-create'),
    path('books/detail/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('books/update/<int:pk>/', BookUpdateAPIView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteAPIView.as_view(), name='book-delete'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # Token authentication endpoint
]




