from django.urls import path
from .views import *


urlpatterns = [
    path('', homePage_view, name='home'),
    path('create_post', create_post_view, name='create_post'),
    
    path('add_ingredients_and_steps/<int:recipeId>', add_ingredients_and_steps_view, name='add_ingredients_and_steps'),
    path('add_image/<int:recipeId>', add_images_views, name='add_image'),
    
    path('<str:slug>', detail_post_view, name='post_detail'),
]