from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.

def homePage_view(request):
    return render(request, 'main/home.html')


def detail_post_view(request):
    return render(request, 'main/post_detail.html')



@login_required
def create_post_view(request):
    
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            RecipePost = form.save(commit=False)
            RecipePost.author = request.user
            RecipePost.save()
            return redirect('add_ingredients_and_steps', recipeId = RecipePost.pk)
        
        return render(request, 'main/create_post.html', {'form':form})
    
    return render(request, 'main/create_post.html', {'form':  form})

@login_required
def add_ingredients_and_steps_view(request, recipeId):
    recipe_id = get_object_or_404(RecipePost, pk = recipeId)
    
    ingredient_form = AddIngredientForm()
    step_form = AddStepsForm()
    image_form = AddImageForm()
    
    context = {
        "ingrediend_form" : ingredient_form,
        "step_form" : step_form,
        "image_form" : image_form
    }
    
    if request.method == 'POST':
        ingredient_form = AddIngredientForm(request.POST)
        step_form = AddStepsForm(request.POST)
        image_form = AddImageForm(request.POST)
        
        if 'add_ingredient' in request.POST and ingredient_form.is_valid():
            ingredient = ingredient_form.save(commit=False)
            ingredient.recipe = recipe_id
            ingredient.save()
            ingredient_form = AddIngredientForm()
        elif 'add_step' in request.POST and step_form.is_valid():
            step = step_form.save(commit=False)
            step.recipe = recipe_id
            step.save()
            step_form = AddStepsForm()
        elif 'add_image' in request.POST and image_form.is_valid():
            image = image_form.save(commit=False)
            image.recipe = recipe_id
            image.save()
            image_form = AddImageForm() 
        elif 'finish' in request.POST:
            return redirect('home')
    return render(request, 'main/add_ingredients_and_steps.html', context)
 


        
    