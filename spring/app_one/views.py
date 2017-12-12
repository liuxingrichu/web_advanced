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
            return redirect("http://www.baidu.com")
        else:
            error_message = "用户名或密码错误"
    return render(request, 'login.html', {'error_message': error_message})
