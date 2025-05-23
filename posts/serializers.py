# posts/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post


class PostSerialier(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
            
        )
        
        model = Post
        
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ("id", "username", )