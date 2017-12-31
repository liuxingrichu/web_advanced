from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.urls import reverse


# Create your views here.

def index(request, name):
    print(type(request))
    from django.core.handlers.wsgi import WSGIRequest
    for k, v in request.environ.items():
        print("%s: %s" % (k, v))
    print(request.environ.get('HTTP_USER_AGENT'))
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


def submaster(request):
    return render(request, 'submaster.html')


def submaster1(request):
    return render(request, 'submaster1.html')


def simple(request):
    name = "Tom"
    return render(request, 'simple.html', {'name': name})
