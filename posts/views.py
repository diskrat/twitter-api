from rest_framework import viewsets,mixins
from rest_framework import permissions

from django.contrib.auth.models import User
from posts.models import Post
from posts.serializers import PostSerializer,UserSerializer,RegistrationSerializer
from posts.permissions import IsOwnerOrReadOnly

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    serializer_class=PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class RegistrationViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset=User.objects.all()
    serializer_class=RegistrationSerializer
    