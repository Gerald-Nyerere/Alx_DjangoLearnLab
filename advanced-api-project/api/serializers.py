from rest_framework import serializers
from .models import Book,Author
from datetime import datetime

# Serializer for the Book model
# This converts Book model instances to JSON and validates incoming data
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Validates that the publication year is not in the future
    def validate(self, data):
        current_year = datetime.now().year

        if data.get('publication_year') and data['publication_year'] > current_year:
            raise serializers.ValidationError("Year cannot be in the future.")

        return data

# Serializer for the Author model
# This includes a nested relationship to show books by the author
class AuthorSerializer(serializers.ModelSerializer):
    # Display books as nested objects under each author
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['name']

       