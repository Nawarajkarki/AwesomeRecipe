from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import *
from main.models import *

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'Users/signup.html', {'form':form})
    else:
        form = SignUpForm()
    return render(request, 'Users/signup.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("okey")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("logedin")
                return redirect('home')
            else:
                print("User not authenticated")
                print(form.errors)
                return render(request, 'User/login.html', {'form' : form})
    else:
        form = AuthenticationForm()
    return render(request, 'Users/login.html', {'form': form})


def user_profile(request, username):
    
    recipes = RecipePost.objects.filter(author__username = username).order_by('-posted_at')
    author = get_object_or_404(User, username=username)
    
    
    context = {
        'author' : author,
        'user' : request.user,
        'recipes' : recipes
    }
    
    return render(request, 'Users/user_profile.html', context)