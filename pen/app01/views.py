from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect


# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == '123':
            request.session['username'] = user
            request.session['is_login'] = True
            if request.POST.get('timeout', None) == '1':
                request.session.set_expiry(10)
            return redirect('/index/')
        else:
            return render(request, 'login.html')


def index(request):
    if request.session.get('is_login', None):
        username = request.session['username']
        return render(request, 'index.html', {'username': username})
    else:
        return HttpResponse('inform wrong')


def logout(request):
    request.session.clear()
    return render(request, 'login.html')


import inspect


class Foo:
    def render(self):
        print('%s.%s' % (self.__class__.__name__, inspect.stack()[0][3]))
        return HttpResponse('ok')


def middle(request):
    print('views.py %s' % inspect.stack()[0][3])
    return Foo()


from django.views.decorators.cache import cache_page


# @cache_page(10)
def cache(request):
    import time
    cur_time = time.time()
    return render(request, 'cache.html', {'cur_time': cur_time})


from app01 import models


def signal(request):
    obj = models.UserInfo(username='Emma')
    print('start')
    obj.save()

    models.UserInfo.objects.create(username='Wilson')
    print('end')

    from sg import pizza_done

    pizza_done.send(sender="asdfasdf", toppings=123, size=456)
    return HttpResponse('ok')


from django import forms


class FM(forms.Form):
    user = forms.CharField(error_messages={'required': '用户名不能为空.'})
    pwd = forms.CharField(
        max_length=12,
        min_length=6,
        error_messages={'required': '密码不能为空.', 'min_length': '密码长度不能小于6',
                        "max_length": '密码长度不能大于12'}
    )
    email = forms.EmailField(
        error_messages={'required': '邮箱不能为空.', 'invalid': "邮箱格式错误"})


def fm(request):
    if request.method == 'GET':
        obj = FM()
        return render(request, 'fm.html', {'obj': obj})
    elif request.method == 'POST':
        obj = FM(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
        else:
            print(obj.errors)
            print(obj.errors.as_json())
            print(obj.errors['user'])
            print(obj.errors['user'][0])
            return render(request, 'fm.html', {'obj': obj})
        return redirect('/fm/')
