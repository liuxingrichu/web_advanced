from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse


# Create your views here.

def login(request):
    models.UserGroup.objects.create(caption="monitor")
    # 时间更新不起作用
    models.UserGroup.objects.filter(uid=2).update(caption="new")
    # 时间更新：OK
    obj = models.UserGroup.objects.filter(uid=1).first()
    obj.caption = "CEO"
    obj.save()
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
        group_list = models.UserGroup.objects.all()
        return render(request, 'user_info.html',
                      {'user_list': user_list, 'group_list': group_list})
    elif request.method == "POST":
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        e = request.POST.get("email")
        group = request.POST.get("user_group_id")
        models.UserInfo.objects.create(username=u, password=p, email=e,
                                       user_group_id=group)
        return redirect('/monitor/user_info')


def user_detail(request, nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    group_obj = models.UserGroup.objects.filter(uid=obj.user_group_id).first()
    # 仅获取一条信息，但id不存在，会报错
    # models.UserInfo.objects.get(id=nid)
    return render(request, 'user_detail.html',
                  {'obj': obj, 'group_obj': group_obj})


def user_del(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/monitor/user_info')


def user_edit(request, nid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        group_list = models.UserGroup.objects.all()
        return render(request, 'user_edit.html',
                      {"obj": obj, "group_list": group_list})
    elif request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("password")
        e = request.POST.get("email")
        uid = request.POST.get("group_id")
        models.UserInfo.objects.filter(id=nid).update(username=u, password=p,
                                                      email=e,
                                                      user_group_id=uid)
        return redirect('/monitor/user_info')


from app02 import models


def orm(request):
    # 增
    # models.UserInfo.objects.create(username='root', password='123')
    #
    # dict_user = {'username': 'Lucy', 'password': '123'}
    # models.UserInfo.objects.create(**dict_user)
    #
    # obj = models.UserInfo(username='Tom', password='123')
    # obj.save()

    # 查
    # result = models.UserInfo.objects.all()
    # result = models.UserInfo.objects.filter(username='Tom')
    # # result的类型是QuerySet，是Django提供的，类似列表
    # for item in result:
    #     print(item.id, item.username, item.password)
    # print(result)

    # 删
    # models.UserInfo.objects.filter(username='Tom').delete()
    # models.UserInfo.objects.filter(id=1).delete()
    # models.UserInfo.objects.all().delete()

    # 改
    # models.UserInfo.objects.all().update(password=999)
    # models.UserInfo.objects.filter(id=7).update(password=666)

    models.UserInfo.objects.create(
        username='Spring',
        password='123',
        email='springcom',
        user_group_id=1
    )

    models.UserInfo.objects.create(
        username='Spring1',
        password='123',
        email='spring@163.com',
        user_group=models.UserGroup.objects.filter(uid=1).first()
    )

    return HttpResponse('orm')
