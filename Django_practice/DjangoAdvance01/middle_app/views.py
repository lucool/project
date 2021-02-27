from django.http import HttpResponse
from django.shortcuts import render


def hello_view(request,name):
    return HttpResponse("<h3>" + name + ",你好</h3>")


def visit_view(request):
    visit_count = request.visit_count   #  获取访问次数
    return HttpResponse("<h3 style='color:green'>恭喜，这是第" + str(visit_count) + "次访问</h3>")
