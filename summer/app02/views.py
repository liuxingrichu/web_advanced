from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        # 在数据库中执行 select * from user where username='x' and password='x'
        return render(request, 'login.html')
    else:
        return redirect("/index")
