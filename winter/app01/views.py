from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.urls import reverse


# Create your views here.

def index(request, name):
    print(name)
    return HttpResponse('OK')


def home(request):
    home1 = reverse("m1:HOME")
    home2 = reverse("m2:HOME")
    if request.path_info == home1:
        print(home1)
        return render(request, 'home1.html')
    elif request.path_info == home2:
        print(home2)
        return render(request, 'home2.html')
    else:
        return HttpResponse('home')
