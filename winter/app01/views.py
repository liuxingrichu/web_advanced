from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe


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


LIST = []
for i in range(1, 100):
    LIST.append(i)


def page(request):
    if request.method == "GET":
        current_page = request.GET.get('p', 1)
        current_page = int(current_page)
        all_count = len(LIST)
        start = (current_page - 1) * 10
        end = current_page * 10
        data = LIST[start:end]
        count, remainder = divmod(all_count, 10)
        if remainder:
            count += 1
        page_list = []
        for i in range(1, count+1):
            if i == current_page:
                temp = "<a class='page active' href='/page/?p=%s'>%s</a>" % (i, i)
            else:
                temp = "<a class='page' href='/page/?p=%s'>%s</a>" % (i, i)
            page_list.append(temp)
        page_str = "".join(page_list)
        page_str = mark_safe(page_str)
        return render(request, 'page.html',
                      {"data": data, 'page_str': page_str})
