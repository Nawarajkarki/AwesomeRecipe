from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *



class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']