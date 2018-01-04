from django.shortcuts import render
from django.shortcuts import redirect
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


from  utils import pagination

LIST = []
for i in range(500):
    LIST.append(i)


def page(request):
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)
    val = request.COOKIES.get('per_page_count')
    print('val: %s' % val)
    val = int(val)
    page_obj = pagination.Page(current_page, len(LIST), val)
    data = LIST[page_obj.start:page_obj.end]
    page_str = page_obj.page_str("/page/")
    return render(request, 'page.html',
                  {"data": data, 'page_str': page_str})


user_info = {
    'spring': {'pwd': "spring"},
    'summer': {'pwd': 'summer'},
}


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        info = user_info.get(u)
        if not info:
            return render(request, 'login.html')
        if info['pwd'] == p:
            res = redirect('/welcome')
            res.set_cookie('username', u)
            # res.set_cookie('username', u, max_age=10)
            # from datetime import datetime, timedelta
            # expire_time = datetime.utcnow() + timedelta(seconds=5)
            # res.set_cookie('username', u, expires=expire_time)
            res.set_cookie('key', 'value', httponly=True)
            return res
        else:
            return render(request, 'login.html')


def welcome(request):
    v = request.COOKIES.get('username')
    if not v:
        return render(request, 'login.html')
    return render(request, 'welcome.html', {'current_username': v})
