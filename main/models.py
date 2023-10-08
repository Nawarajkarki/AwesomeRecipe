from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


def user_directory_path(instance, filename):
    return '{0}/recipe/{1}/{2}'.format(instance.recipe.author.username, instance.recipe.slug, filename)


class RecipePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    posted_at = models.DateTimeField(auto_now_add=True)
    title = models.Char0Field(max_length=200)
    description = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from='title', unique=True)
    
    def __str__(self):
        return self.title
    

class Ingredient(models.Model):
    recipe = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name= 'ingredients')
    ingredient = models.CharField(max_length=200)
    quantity = models.CharField(max_length=50)
    
    def __str__(self):
        return self.ingredient
    
    
class Step(models.Model):
    recipe = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name= 'steps')
    step = models.CharField(max_length=500)
    
    def __str__(self):
        return self.step
    
class RecipeImage(models.Model):
    recipe = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name= 'images')
    images = models.ImageField(upload_to=user_directory_path)
    
    
    
# The Following model is for Bookmarked posts
class Saved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved')
    recipe = models.ForeignKey(RecipePost, on_delete=models.CASCADE, related_name='saved')
    
    class Meta:
        unique_together = ('user', 'recipe')
        
    def __str__(self):
        return f"{self.user.username} saved {self.recipe.pk}"