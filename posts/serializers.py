# posts/serializers.py

from rest_framework import serializers

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
        