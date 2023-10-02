from django.urls import path
from .views import *


urlpatterns = [
    path('', homePage_view, name='home'),
]