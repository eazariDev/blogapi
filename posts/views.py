# posts/views.py

from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerialier, UserSerializer
from .permissions import IsAuthorOrReadOnly

from django.contrib.auth import get_user_model


# class PostList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly, )
#     queryset = Post.objects.all()
#     serializer_class = PostSerialier
    

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    
#     # permission_classes = (permissions.IsAdminUser, )
    
#     permission_classes = (IsAuthorOrReadOnly, )
#     queryset = Post.objects.all()
#     serializer_class = PostSerialier
    
    
    
# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
    

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerialier
    
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser,]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer