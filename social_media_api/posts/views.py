from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post  # Assuming Post model is already defined in your posts app
from django.contrib.auth import get_user_model

# Custom pagination class
class PostPagination(PageNumberPagination):
    page_size = 10  # Limit to 10 posts per page
    
# Viewset for Post: Handles all CRUD operations
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # Fetch all posts
    serializer_class = PostSerializer  # Define which serializer to use
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access for unauthenticated users
    pagination_class = PostPagination  # Enable pagination
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_fields = ['title', 'content']  # Allow filtering by title or content

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set the author to the current user when creating a post


# Viewset for Comment: Handles all CRUD operations
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # Fetch all comments
    serializer_class = CommentSerializer  # Define which serializer to use
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access for unauthenticated users

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set the author to the current user when creating a comment

User = get_user_model()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    # Get the users that the current user follows
    followed_users = request.user.following.all()

    # Get posts made by followed users, ordered by creation date (most recent first)
    posts = Post.objects.filter(user__in=followed_users).order_by('-created_at')

    # Serialize the posts (assuming a PostSerializer is already defined)
    serializer = PostSerializer(posts, many=True)

    # Return the serialized posts in the response
    return Response(serializer.data)


