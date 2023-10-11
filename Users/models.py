from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


# Users personal files uploading directory
def user_directory_path(instance, filename):
    return '{0}/profile_images/{1}'.format(instance.username, filename)


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username or self.display_name

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50, null=True, blank=True)
    display_picture = models.ImageField(upload_to=user_directory_path, null = True , blank = True)
    cover_picture = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    followers_count = models.PositiveIntegerField(default=0)  
    city = models.CharField(max_length=100, null=True, blank=True)
    about_user = models.CharField(max_length=600)
    
    
    def __str__(self):
        return self.user.username
    

    

class Followers(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    
    def __str__(self):
        return self.follower.username + ' follows ' + self.following.username
    
