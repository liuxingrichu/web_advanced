from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

from app01 import models


def add_business(request):
    models.Business.objects.create(name='研发部')
    models.Business.objects.create(name='测试部')
    models.Business.objects.create(name='运维部')
    models.Business.objects.create(name='营销部')
    return HttpResponse('ok')
