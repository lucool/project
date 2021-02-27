from django.shortcuts import render, redirect
from django.urls import reverse


def register_view(request):
    if request.method == "GET":
        return render(request,'register_app/register.html')
    elif request.method == "POST":
        regname = request.POST.get("regname")
        regpwd = request.POST.get("regpwd")
        #return redirect(reverse("reg:suc",args=(regname,)))   # 重定向+反向解析
        return redirect(reverse("reg:suc", kwargs={"username":regname}))  # 重定向+反向解析


def success_view(request,username):
    return render(request,'register_app/success.html',locals())