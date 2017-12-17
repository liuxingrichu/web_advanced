from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse


# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        # 在数据库中执行 select * from user where username='x' and password='x'
        return render(request, 'login.html')
    else:
        return redirect("/index")


from app02 import models


def orm(request):
    # 增
    models.UserInfo.objects.create(username='root', password='123')

    dict_user = {'username': 'Lucy', 'password': '123'}
    models.UserInfo.objects.create(**dict_user)

    obj = models.UserInfo(username='Tom', password='123')
    obj.save()

    # 查
    result = models.UserInfo.objects.all()
    result = models.UserInfo.objects.filter(username='Tom')
    # result的类型是QuerySet，是Django提供的，类似列表
    for item in result:
        print(item.id, item.username, item.password)
    print(result)

    # 删
    models.UserInfo.objects.filter(username='Tom').delete()
    models.UserInfo.objects.filter(id=1).delete()
    models.UserInfo.objects.all().delete()

    # 改
    models.UserInfo.objects.all().update(password=999)
    models.UserInfo.objects.filter(id=7).update(password=666)

    return HttpResponse('orm')
