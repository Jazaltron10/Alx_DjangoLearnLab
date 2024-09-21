# accounts/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer

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
