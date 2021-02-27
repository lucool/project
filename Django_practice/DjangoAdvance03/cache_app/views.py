import time

from django.core.cache import cache,caches
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


def fruits_view(request):
    key = "fruit:cache"
    data = cache.get(key)   # cache用来操作默认(default)缓存配置,先试图从缓存中获取数据
    if data:    # 如果缓存中存在该数据
        print("缓存命中了~~~")
        return HttpResponse(data)
    else:       # 如果缓存中没有查询到数据
        print("缓存中没有，模拟耗时操作......")
        time.sleep(3)
        fruits = ["橙子","苹果","香蕉","猕猴桃"]
        response = render(request,'cache_app/fruits.html',{"fruits":fruits})
        cache.set(key,response.content,timeout=30)   # 将响应内容（渲染出的模板内容）存储到缓存中
        return response


def fruits_redis_view(request):
    key = "fruit:cache"
    c = caches["my_redis_cache"]    # 获取配置中key为“my_redis_cache”的缓存配置信息
    data = c.get(key)  # 尝试从配置的缓存中获取数据
    if data:  # 如果缓存中存在该数据
        print("缓存命中了~~~")
        return HttpResponse(data)
    else:  # 如果缓存中没有查询到数据
        print("缓存中没有，模拟耗时操作......")
        time.sleep(3)
        fruits = ["橙子", "苹果", "香蕉", "猕猴桃"]
        response = render(request, 'cache_app/fruits.html', {"fruits": fruits})
        c.set(key, response.content, timeout=30)  # 将响应内容（渲染出的模板内容）存储到缓存中
        return response


@cache_page(timeout=30,cache="my_redis_cache",key_prefix="python1904")
def page_view(request):
    print("缓存中没有，模拟耗时操作......")
    time.sleep(3)
    fruits = ["菠萝", "西瓜", "榴莲", "荔枝"]
    return render(request,'cache_app/fruits.html',{"fruits":fruits})