# accounts/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Importing the CustomUser model
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    # Add a method to handle GET requests
    def get(self, request, *args, **kwargs):
        return Response({"message": "Register form (or page) is here"}, status=200)

class LoginView(ObtainAuthToken):
    # Custom login view to return token and user info
    def post(self, request, *args, **kwargs):
        response = super(LoginView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = UserSerializer(token.user)
        return Response({
            'token': token.key,
            'user': user.data
        })

    # Add a method to handle GET requests
    def get(self, request, *args, **kwargs):
        return Response({"message": "Login form (or page) is here"}, status=200)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Return the current user
        return self.request.user
    
    # Add a method to handle GET requests
    def get(self, request, *args, **kwargs):
        return Response({"message": "Profile page is here"}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    # Fetch the user that the current user wants to follow
    user_to_follow = get_object_or_404(User, id=user_id)
    
    # Prevent following yourself
    if request.user == user_to_follow:
        return JsonResponse({'error': 'You cannot follow yourself'}, status=400)
    
    # Add the user to the current user's 'following' list
    request.user.following.add(user_to_follow)
    
    # Return a success message
    return JsonResponse({'message': f'You are now following {user_to_follow.username}'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    # Fetch the user that the current user wants to unfollow
    user_to_unfollow = get_object_or_404(User, id=user_id)
    
    # Remove the user from the current user's 'following' list
    request.user.following.remove(user_to_unfollow)
    
    # Return a success message
    return JsonResponse({'message': f'You have unfollowed {user_to_unfollow.username}'})
