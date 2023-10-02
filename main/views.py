from django.shortcuts import render


# Create your views here.

def homePage_view(request):
    return render(request, 'main/home.html')