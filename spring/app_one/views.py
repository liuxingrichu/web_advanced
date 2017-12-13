from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.

def login(request):
    """
    :param request: 包含用户提交的所有信息
    :return:
    """
    error_message = ""
    # request.method 获取用户提交方式
    if request.method == "POST":
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        if user == 'root' and pwd == '123':
            return redirect("/home")
        else:
            error_message = "用户名或密码错误"
    return render(request, 'login.html', {'error_message': error_message})


USER_LIST = [
    {"id":1, "username": "Tom", "email": "tom@163.com", "gender": "M"},
    {"id":2, "username": "Lucy", "email": "lucy@163.com", "gender": "F"},
    {"id":3, "username": "Seven", "email": "seven@163.com", "gender": "M"},
]


def home(request):
    if request.method == "POST":
        user = request.POST.get("username")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        temp = {"username": user, "email": email, "gender": gender}
        USER_LIST.append(temp)
    return render(request, 'home.html', {'user_list': USER_LIST})
