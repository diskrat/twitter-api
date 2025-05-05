from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    contents = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user','post')
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.pk is None:
            self.post.like_count += 1
            self.post.save()

    def delete(self,*args,**kwargs):
        super().delete(*args,**kwargs)
        self.post.like_count-=1
        
class Follow(models.Model):
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    class Meta:
        unique_together = ('following','follower')