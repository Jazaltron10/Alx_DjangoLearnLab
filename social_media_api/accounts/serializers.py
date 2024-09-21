from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()  # Fetches the CustomUser model

class UserSerializer(serializers.ModelSerializer):
    # Serializer for user model that includes bio, profile_picture, and followers
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']


class RegisterSerializer(serializers.ModelSerializer):
    # Serializer used for user registration
    password = serializers.CharField(write_only=True)  # Ensure password uses CharField

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user using create_user, which handles password hashing
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        Token.objects.create(user=user)  # Create token upon registration
        return user
