from rest_framework import serializers
from .models import Book
from users.models import User

class BookSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Book
        fields = ("name", "description", "user")

    
    def create(self, validated_data):
        user = validated_data.pop("user")
        author = user.author.first()
        book = Book.objects.create(**validated_data, author=author)
        
        return book