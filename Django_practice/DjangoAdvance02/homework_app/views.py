from django.shortcuts import render, redirect
from django.urls import reverse


def login_view(request):
    if request.method == "GET":
        if request.session.get("msg"):  # 先判断会话中是否有消息
            messages = request.session.get("msg")   # 从会话中取出消息
            del request.session["msg"]  # 删除会话中的msg属性
        return render(request,'homework_app/login.html',locals())
    elif request.method == "POST":
        logname = request.POST.get("logname")
        logpwd = request.POST.get("logpwd")
        if logname == "tom" and logpwd == "123456":   # 如果验证通过
            request.session["username"] = logname
            return redirect(reverse("home:suc"))   # 重定向到成功页面
        else:   # 如果验证未通过
            request.session["msg"] = "用户名或密码错误，请重新输入登录信息！"  # 在session中暂存消息
            return redirect(reverse("home:log"))   # 重定向到登录页面


def success_view(request):
    return render(request,'homework_app/success.html')