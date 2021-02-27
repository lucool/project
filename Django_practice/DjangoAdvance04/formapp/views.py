from django.shortcuts import render, redirect
from django.urls import reverse

from formapp.forms import UserForm


def register_view(request):
    if request.method == "GET":
        userform = UserForm()   # 创建一个空的表单对象
        return render(request,'formapp/register.html',locals())
    elif request.method == "POST":
        userform = UserForm(request.POST)  # 将POST请求中的数据封装到UserForm对象中
        if userform.is_valid():  # 验证表单数据是否有效
            regname = userform.cleaned_data["regname"]
            regpwd = userform.cleaned_data["regpwd"]
            reghome = userform.cleaned_data["reghome"]
            regsex = userform.cleaned_data["regsex"]
            print("注册用户名：",regname,"；注册密码：",regpwd,"籍贯：",reghome,"；性别：",regsex)
            return redirect(reverse("form:suc"))
        else:
            return redirect(reverse("form:reg"))


def success_view(request):
    return render(request,'formapp/success.html')


