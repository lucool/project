from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def register_view(request):
    if request.method == "GET":
        return render(request,'csrf_app/register.html')
    elif request.method == "POST":
        regname = request.POST.get("regname")
        return redirect(reverse("csrf:suc",args=(regname,)))


def success_view(request,regname):
    return render(request,'csrf_app/success.html',locals())

@csrf_exempt
def login_view(request):
    if request.method == "GET":
        return render(request,'csrf_app/login.html')
    elif request.method == "POST":
        logname = request.POST.get("logname")
        return redirect(reverse("csrf:wel",args=(logname,)))


def welcome_view(request,logname):
    return render(request,'csrf_app/welcome.html',locals())