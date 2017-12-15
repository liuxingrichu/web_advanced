from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect


# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        user = request.POST.get("username")
        pwd = request.POST.get("pwd")
        if user == "root" and pwd == "123":
            return redirect("/index")
    else:
        return redirect("/login")


def index(request):
    return HttpResponse("index")
