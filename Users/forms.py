from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

from django.contrib.auth import authenticate




# This is Signup / Use Registration Form 
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs = {'class' : 'input_area', 'placeholder':'Username', 'required' : True }),
            'email' : forms.EmailInput(attrs = {'class' : 'input_area', 'placeholder' : 'Email address'}),
            'password1' : forms.PasswordInput(attrs ={'class' : 'input_area', 'placeholder' : 'Password'}),
            'password2' : forms.PasswordInput(attrs ={'class' : 'input_area', 'placeholder' : 'Confirm Password'})
        }
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email.lower()
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username already exists')
        return username.lower()
    
    def clean_password(self):
        cleaned_data = super().clean()
        password1 = self.cleaned_data('password1')
        password2 = self.cleaned_data('password2')
        if password1 != password2:
            raise forms.ValidationError('Passwords donot match.')
        return password1
    
    
