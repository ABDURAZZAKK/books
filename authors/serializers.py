from rest_framework import serializers
from users.models import User
from users.serializers import UserCreateSerializer
from .models import Author


class CreateAutorSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()

    class Meta:
        model = Author
        fields = ("first_name", "second_name", "birth_at", "user")
        

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create_user(**user_data)
        author = Author.objects.create(**validated_data, user=user)
        
        return author