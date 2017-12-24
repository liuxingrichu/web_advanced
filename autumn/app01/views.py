from django.shortcuts import render
from django.shortcuts import redirect
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


def set_host(request):
    if request.method == "GET":
        v1 = models.Business.objects.filter(id__gt=0)
        return render(request, 'set_host.html', {'v1': v1})
    elif request.method == "POST":
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        b = request.POST.get('business_name')
        models.Host.objects.create(hostname=hostname, ip=ip, port=port, b_id=b)
        return redirect('/get_host')


def get_host(request):
    v1 = models.Host.objects.all()
    return render(request, 'get_host.html', {'v1': v1})
