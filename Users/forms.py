from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

from django.contrib.auth import authenticate



class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email.lower()
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username already exists")
        return username.lower()
    
    def clean_password(self):
        cleaned_data = super().clean()
        password1 = self.cleaned_data('password1')
        password2 = self.cleaned_data('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords donot match.")
        return password1
    
    


class UserLoginForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['email', 'password']
        
        
    def clean(self):
       cleaned_data = super().clean()
       email = cleaned_data.get('email')
       password = cleaned_data.get('password')
       
       # Authenticate the user
       user = authenticate(request=None, username=email, password=password)
       
       if user is None:
           raise forms.ValidationError("Invalid email or password")
       return cleaned_data