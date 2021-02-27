from django.shortcuts import render, redirect
from django.urls import reverse

from form_app.forms import RegisterForm


def register_view(request):
    if request.method == "GET":
        regform = RegisterForm()   # 实例化表单对象
        return render(request,'form_app/register.html',locals())
    elif request.method == "POST":
        regform = RegisterForm(request.POST) # 将POST参数封装到表单对象中
        if regform.is_valid():  # 验证表单数据是否有效
            regname = regform.cleaned_data["regname"]
            regpwd = regform.cleaned_data["regpwd"]
            reghome = regform.cleaned_data["reghome"]
            regsex = regform.cleaned_data["regsex"]
            print("注册名是：",regname,";注册密码是：",regpwd,"；籍贯是：",reghome,"；性别是：",regsex)
            return redirect(reverse("form:suc"))   # 重定向到成功页面
        else:
            return redirect(reverse("form:reg"))  # 重定向到成功页面


def success_view(request):
    return render(request,'form_app/success.html')