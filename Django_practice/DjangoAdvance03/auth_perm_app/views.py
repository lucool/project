from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def login_view(request):
    if request.method == "GET":
        return render(request,'auth_perm_app/login.html')
    elif request.method == "POST":
        logname = request.POST.get("logname")
        logpwd = request.POST.get("logpwd")
        user = authenticate(username=logname,password=logpwd)   # 验证用户，还会检验is_active字段
        if user is not None:
            login(request,user)   # 会将User的ID存入session中
            return redirect(reverse("ap:students"))
        else:
            return redirect(reverse('ap:log'))


def students_view(request):
    return render(request,'auth_perm_app/students.html')


@permission_required(perm="auth_perm_app.change_student",login_url="/ap/login/")   # 检验是否具有更新学生的权限
def update_view(request):
    return HttpResponse("<h3 style='color:blue'>你具有更新学生的权限~~~</h3>")