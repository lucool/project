from django.http import HttpResponse
from django.shortcuts import render


def go_a(request,fruit,color):
    return render(request,'reverse_app/a.html',locals())


def handle_a(request,f,c):
    result = "水果名称为：" + f + "；水果颜色为：" + c
    return HttpResponse(result)