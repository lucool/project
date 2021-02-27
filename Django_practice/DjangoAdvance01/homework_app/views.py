import uuid

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from homework_app.models import User


def login_view(request):
    if request.method == "GET":
        return render(request,'homework_app/login.html')
    elif request.method == "POST":
        logname = request.POST.get("logname")
        logpwd = request.POST.get("logpwd")
        if logname == "tom" and logpwd == "123456":
            request.session["username"] = logname # 在会话中添加一个属性
            return redirect(reverse("home:suc"))
        else:
            return redirect(reverse("home:login"))


def success_view(request):
    if not request.session.get("username"):   # 进行登录验证
        return redirect(reverse("home:login"))
    return render(request,'homework_app/success.html')


@csrf_exempt
def login_token_view(request):
    if request.method == "POST":
        logname = request.POST.get("logname")
        logpwd = request.POST.get("logpwd")
        users = User.objects.filter(username=logname,password=logpwd)
        if users:
            user = users.first()
            token =  uuid.uuid4().hex   # 创建token
            user.token = token # 更新token
            user.save()
            data = {
                "code":"200",
                "msg":"登录成功",
                "token":token
            }
            return JsonResponse(data)
        else:
            data = {
                "code": "404",
                "msg": "登录失败"
            }
            return JsonResponse(data)


def success_token_view(request):
    token = request.GET.get("token")
    try:
        user = User.objects.get(token=token)  # get只能返回一条记录，否则报错
        data = {
            "code": "208",
            "msg": "可以访问成功函数~~~",
        }
        return JsonResponse(data)
    except:
        data = {
            "code": "408",
            "msg": "您还未登录，不能访问成功函数！"
        }
        return JsonResponse(data)