from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse


def register_view(request):
    if request.method == "GET":
        return render(request,'auth_perm_app/register.html')
    elif request.method == "POST":
        regname = request.POST.get("regname")
        regpwd = request.POST.get("regpwd")
        regemail = request.POST.get("regemail")
        new_user = User.objects.create_user(username=regname,password=regpwd,email=regemail)  # 创建对象，并插入数据库表
        return redirect(reverse("ap:log"))


def login_view(request):
    if request.method == "GET":
        return render(request,'auth_perm_app/login.html')
    elif request.method == "POST":
        logname = request.POST.get("logname")
        logpwd = request.POST.get("logpwd")
        user = authenticate(username=logname,password=logpwd)   # 通过用户名和密码进行用户认证,该方法也会自动检查is_active标志位
        print("user=",user)
        if user is not None:    #  如果认证成功
            login(request,user)  # login向session中添加User对象的ID, 便于对用户进行跟踪
            return redirect(reverse("ap:wel"))
        else:
            return redirect(reverse("ap:log"))


@login_required(login_url="/ap/login/")   # 该装饰装饰的函数必须要登录后，才能执行，否则重定向到login_url参数指向的路由
def welcome_view(request):
    return render(request,'auth_perm_app/welcome.html')


def logout_view(request):
    logout(request)   # 登出
    return redirect(reverse("ap:log"))

