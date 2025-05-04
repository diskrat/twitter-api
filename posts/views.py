from rest_framework import viewsets,mixins
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from posts.models import Post,Like
from posts.serializers import PostSerializer,UserSerializer,RegistrationSerializer,LikeSerializer
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
    
class LikeViewSet(mixins.CreateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset=Like.objects.all()
    serializer_class=LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        context['post'] = post
        return context
    