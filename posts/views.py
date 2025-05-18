# posts/views.py

from rest_framework import generics 

from .models import Post
from .serializers import PostSerialier


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialier
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialier
    
    