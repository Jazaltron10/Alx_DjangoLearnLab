from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer

# Importing the CustomUser model
User = get_user_model()

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
        

# View to generate a feed based on the users the current user follows
class UserFeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access the feed

    def get(self, request, *args, **kwargs):
        # Get the users the current user is following
        following_users = request.user.following.all()

        # Filter posts by the authors the current user follows and order them by creation date (newest first)
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize the posts to return them as JSON
        serializer = PostSerializer(posts, many=True)

        # Return the serialized posts as the feed response
        return Response(serializer.data, status=200)
