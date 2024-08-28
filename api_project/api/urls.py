from django.urls import include, path 
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),
    # path("", BookList.as_view(), name="home"),
]



