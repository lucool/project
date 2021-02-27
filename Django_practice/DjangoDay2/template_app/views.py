from django.shortcuts import render
from template_app.po import Person
from datetime import datetime


def show_var(request):
    per = Person("tom",20)
    s = "hello"
    fruits = ["apple","orange","banana"]
    mydict = {"color":"yellow","country":"China"}
    print("locals()=",locals())
    return render(request,'template_app/vars/hello.html', locals())


def if_view(request,score):
    return render(request,'template_app/tags/if_demo.html',{"score":score})


def for_view(request):
    links = ["百度","搜狐","阿里巴巴","腾讯"]
    sports = []
    return render(request,'template_app/tags/for_demo.html',locals())


def child_view(request):
    return render(request,'template_app/extends/child.html',{"info":"西安加油！"})


def filter_view(request):
    s = "heLLo"
    t = datetime(2019,10,8,12,15,53)
    score = 55
    return render(request,'template_app/filter/filter_demo.html',locals())

def custom_filter_view(request,number):
    return render(request,'template_app/filter/custom_filter.html',{"number":number})