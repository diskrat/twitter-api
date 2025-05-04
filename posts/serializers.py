from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from posts.models import Post,Like

class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Post
        fields = ['url', 'id', 'owner','contents','like_count']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','posts','url']
        
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,validators=[validate_password])
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model=User
        fields = ['username','email','password']
    
    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  
    class Meta:
        model = Like  
        fields = ['id', 'user', 'post']  
        read_only_fields = ['post'] 

    def create(self,request):
        user = self.context['request'].user
        post = self.context.get('post')
        return Like.objects.create(post=post,user=user)
    