from django.shortcuts import render


# Create your views here.

def homePage_view(request):
    return render(request, 'main/home.html')


def detail_post_view(request):
    return render(request, 'main/post_detail.html')