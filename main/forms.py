from django import forms
from django.forms import ModelForm

from .models import *



class CreatePostForm(ModelForm):
    class Meta:
        model = RecipePost
        fields = ['title', 'description']
        widgets = {
            'title' : forms.TextInput(attrs = {"class" : "recipe_post", "placeholder" : "Recipe Title"}),
            'description' : forms.Textarea(attrs = {"class" : "recipe_post", "placeholder" : "Recipe Description"})
        }
        
        
class AddIngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient', 'quantity']
        widgets = {
            'ingredient' : forms.TextInput(attrs = {"class" : "recipe_post", "placeholder" : "Recipe ingredient"}),
            'quantity' : forms.TextInput(attrs = {"class" : "recipe_post quantity_input", "placeholder" : "Quantity"})
        }
        
        
        
class AddStepsForm(ModelForm):
    class Meta:
        model = Step
        fields = ['step']
        widgets = {
            'step' : forms.TextInput(attrs = {"class" : "recipe_post", "placeholder" : "Recipe step"}),
        }
        
        
class AddImageForm(ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image']
        

        