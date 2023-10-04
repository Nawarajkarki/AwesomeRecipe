from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import *
# Create your views here.


def signup_view(request, *args, **kwargs):
    form = UserCreateForm()
    
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.save()
            login(request, user)
            return redirect('home')

    else:
        form = UserCreateForm()
    return render(request, 'Users/signup.html', {'form':form})


def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            
            else:
                form.add_error("None, Invalid email or password")
    
    else:
        form = UserLoginForm(request.POST)

    return render(request, 'Users/login.html', {'form':form})


def user_profile(request):
    return render(request, 'Users/user_profile.html')