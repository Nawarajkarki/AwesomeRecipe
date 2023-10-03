from django.urls import path
from .views import *


urlpatterns = [
    path('', homePage_view, name='home'),
    path('post', detail_post_view, name='post_detail'),
]