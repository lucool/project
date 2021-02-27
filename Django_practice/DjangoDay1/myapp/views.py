from django.http import HttpResponse
from django.shortcuts import render


def hello_view(request):   # Django视图函数的第一个参数代表请求对象，必须要写
    return HttpResponse("<h3 style='color:red'>Hello,Django~~~</h3>")



def hi_view(request,country,name):
    return HttpResponse("<h3 style='color:green'>Hi~~~:" + name + "; country:" + country + "</h3>")


def greet_view(request,name):
    result = "<h3>捕获的name参数是：<span style='color:red'>" + name + "</span></h3>"
    return HttpResponse(result)


def welcome_view(request,name,color):
    result = "<h3>name参数值为：" + name + ";color参数值为：" + color + "</h3>"
    return HttpResponse(result)


def url_test_view(request,home,tel):
    result = "<h3>home参数值为：" + home + ";tel参数值为：" + tel + "</h3>"
    return HttpResponse(result)


def convert_view1(request,name,age,uid):
    age += 10
    print("uid参数的类型是：",type(uid),",uid=",uid)
    result = "<h3>name参数值为：" + name + ";10年后的年龄为：" + str(age) + "</h3>"
    return HttpResponse(result)


def convert_view2(request,info,comment):
    result = "<h3>info参数值为：" + info + ";该URL的解释是：" + comment + "</h3>"
    return HttpResponse(result)
