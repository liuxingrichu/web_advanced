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


def index(request):
    return HttpResponse("index")
