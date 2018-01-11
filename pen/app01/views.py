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
    return HttpResponse('ok')
