# posts/views.py

from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerialier
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerialier
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    
    # permission_classes = (permissions.IsAdminUser, )
    
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerialier
    
    