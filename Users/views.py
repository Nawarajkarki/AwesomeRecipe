from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .forms import *
# Create your views here.

def signup(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.username.lower()
            user.email = form.email.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
            return render(request, 'Users/signup.html', {'form': form})
    
    return render(request, 'Users/signup.html', {'form':form})
            
    


def user_profile(request):
    return render(request, 'Users/user_profile.html')