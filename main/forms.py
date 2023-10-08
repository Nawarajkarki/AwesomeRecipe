from django import forms
from django.forms import ModelForm

from .models import *



class CreatePostForm(ModelForm):
    class Meta:
        model = RecipePost
        fields = ['title', 'description']
        
        
class AddIngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient', 'quantity']
        
        
class AddStepsForm(ModelForm):
    class Meta:
        model = Step
        fields = ['step']
        
        
class AddImageForm(ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['images']
        

        