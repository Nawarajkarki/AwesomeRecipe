from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


# Users personal files uploading directory
def user_directory_path(instance, filename):
    return 'media/User_{0}/{1}'.format(instance.pk, filename)


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=50, null=True, blank=True)
    display_picture = models.ImageField(upload_to=user_directory_path, null = True , blank = True)
    cover_picture = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    followers_count = models.PositiveIntegerField(default=0)  
    
    def __str__(self):
        return self.username or self.display_name
    

class Followers(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    
    def __str__(self):
        return self.follower.username + ' follows ' + self.following.username
    
