from django.urls import path
from .views import *


urlpatterns = [
    path('signup', signup_view, name='signup'),
    path('login', login_view, name='login'),
    
    path('<str:username>', user_profile, name='user_profile'),
]