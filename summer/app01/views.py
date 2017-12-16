from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
import os


# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        # v = request.POST.get("city")
        obj = request.FILES.get("file")
        print(type(obj.name), obj.name)
        file_path = os.path.join("upload", obj.name)
        with open(file_path, mode="wb") as f:
            for part in obj.chunks():
                f.write(part)
        return render(request, "login.html")
    else:
        return redirect("/login")


from django.views import View


class Home(View):
    def dispatch(self, request, *args, **kwargs):
        print("before")
        result = super(Home, self).dispatch(request, *args, **kwargs)
        print("after")
        return result

    def get(self, request):
        print(request.method)
        return render(request, 'home.html')

    def post(self, request):
        print(request.method)
        return render(request, 'home.html')


# USER_DICT = {
#     "k1": "v1",
#     "k2": "v2",
#     "k3": "v3",
# }




def index(request):
    return render(request, 'index.html', {"user_dict": USER_DICT})

USER_DICT={
    "1":{"name": "root1", "email": "root1@163.com"},
    "2":{"name": "root2", "email": "root2@163.com"},
    "3":{"name": "root3", "email": "root3@163.com"},
    "4":{"name": "root4", "email": "root4@163.com"},
}

def detail(request):
    nid = request.GET.get("nid")
    detail_info = USER_DICT.get(nid)
    return render(request, "detail.html", {"detail_info":detail_info})