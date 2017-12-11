from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('<h1>CMDB<h1>')

def login(request):
    # f = open('templates/login.html', 'r', encoding='utf-8')
    # data = f.read()
    # f.close()
    # return HttpResponse(data)
    return render(request, 'login.html')