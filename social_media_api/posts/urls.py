from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet)  # Register post routes
router.register(r'comments', CommentViewSet)  # Register comment routes

# Include the router URLs
urlpatterns = [
    path('', include(router.urls)),
]
