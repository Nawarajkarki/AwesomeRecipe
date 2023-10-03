from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


def user_directory_path(instance, filename):
    return 'user_{0}/{1}/recipe/recipe_{0}/{1}'.format(instance.User.id, instance.RecipePost.slug, filename)



class RecipePost(models.Model):
    slug = models.SlugField(max_length=20, unique=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE),
    posted_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
    

class Ingredient(models.Model):
    recipe = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name= 'ingredients')
    ingredients = models.CharField(max_length=200)
    quantity = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
    
class Steps(models.Model):
    recipe = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name= 'steps')
    steps = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
    
class Images(models.Model):
    recipe = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name= 'images')
    images = models.ImageField(upload_to=user_directory_path)