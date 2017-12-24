from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

from app01 import models


def set_business(request):
    models.Business.objects.create(name='研发部')
    models.Business.objects.create(name='测试部')
    models.Business.objects.create(name='运维部')
    models.Business.objects.create(name='营销部')
    return HttpResponse('ok')


def get_business(request):
    # QuerySet类型，元素是对象
    v1 = models.Business.objects.all()
    # QuerySet类型，元素是字典
    v2 = models.Business.objects.all().values('id', 'name')
    # QuerySet类型，元素是元组
    v3 = models.Business.objects.all().values_list('id', 'name')
    return render(request, 'get_business.html', {'v1': v1, 'v2': v2, 'v3': v3})
