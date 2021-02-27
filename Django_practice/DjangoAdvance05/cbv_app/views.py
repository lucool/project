import time

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View


def a(func):     #  该函数装饰器，将要被转化为方法装饰器
    def wrapper(*args,**kwargs):
        print("准备记时......")
        start = time.time()
        result = func(*args,**kwargs)   # 执行被装饰的函数
        end = time.time()
        print("执行共耗时：",(end-start))
        return result
    return wrapper


@method_decorator(a,name="dispatch")
class LoginView(View):

    def dispatch(self, request, *args, **kwargs):
        print("dispatch into...")
        obj = super(LoginView,self).dispatch(request, *args, **kwargs)  # 还是调用父类的dispatch进行方法分派
        print("dispatch end....")
        return obj


    #@method_decorator(a)   # 将a转换为方法装饰器，并对get()方法进行装饰
    def get(self,request):
        print("login get()......")
        time.sleep(3)
        return HttpResponse("<h3 style='color:blue'>Get....</h3>")

    #@method_decorator(a)
    def post(self,request):
        print("login post()......")
        return redirect(reverse("cbv:suc"))


class SuccessView(View):
    def get(self,request):
        return render(request,'cbv_app/success.html')