import time

from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(timeout=30)
def fruits_view(request):
    print("数据库缓存中没有水果信息，等待查询......")
    time.sleep(3)
    fruits = ["菠萝","橙子","西瓜"]
    return render(request,'homeworkapp/fruits.html',locals())


@cache_page(timeout=30,cache="redis_cache")
def students_view(request):
    print("Redis缓存中没有学生信息，等待查询......")
    time.sleep(3)
    students = ["张三","李四","王五"]
    return render(request,'homeworkapp/students.html',locals())