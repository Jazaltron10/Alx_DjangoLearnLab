import datetime  # Importing the datetime module to work with dates
from rest_framework import serializers  # Importing serializers from Django REST Framework
from .models import Author, Book  # Importing the Author and Book models from the current app

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Specify the model to serialize
        fields = ['title', 'publication_year', 'author']  # Specify the fields to include in the serialization
        
    def validate(self, value):
        # Validation method to ensure the publication year is not in the future
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value  # Return the validated value

# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Include related books in the serialized output, making them read-only
    
    class Meta:
        model = Author  # Specify the model to serialize
        fields = ['name', 'books']  # Specify the fields to include in the serialization
