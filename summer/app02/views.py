from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse


# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, 'login1.html')
    elif request.method == "POST":
        error_message = "用户名或密码错误"
        # 在数据库中执行 select * from user where username='x' and password='x'
        username = request.POST.get("username")
        password = request.POST.get("password")
        obj1 = models.UserInfo.objects.filter(username=username,
                                              password=password).first()
        # obj2 = models.UserInfo.objects.filter(username="root", password="999").count()
        if obj1:
            return redirect('/monitor/index1')
        else:
            return render(request, 'login1.html',
                          {"error_message": error_message})
    else:
        return redirect("/index1")


def index(request):
    return render(request, 'index1.html')


def user_info(request):
    if request.method == "GET":
        user_list = models.UserInfo.objects.all()
        # print(user_list.query)
        return render(request, 'user_info.html', {'user_list': user_list})
    elif request.method == "POST":
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        models.UserInfo.objects.create(username=u, password=p)
        return redirect('/monitor/user_info')


def user_detail(request, nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    # 仅获取一条信息，但id不存在，会报错
    # models.UserInfo.objects.get(id=nid)
    return render(request, 'user_detail.html', {'obj': obj})


def user_del(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/monitor/user_info')


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
    # models.UserInfo.objects.filter(username='Tom').delete()
    # models.UserInfo.objects.filter(id=1).delete()
    # models.UserInfo.objects.all().delete()

    # 改
    models.UserInfo.objects.all().update(password=999)
    # models.UserInfo.objects.filter(id=7).update(password=666)

    return HttpResponse('orm')
