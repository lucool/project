import random,redis

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class FirstMiddleware(MiddlewareMixin):   # 自定义中间件类

    def process_request(self,request):    #  每次接收到请求时，自动执行该方法
        print("process_request(FirstMiddleware)......")
        number = random.randint(1,100)
        if number > 80:
            result = "<h3>你被截获了，不能访问！'中奖'数字为：" + str(number) + "</h3>"
            return HttpResponse(result)   # 返回响应

    def process_view(self, request, view, args, kwargs):   #  解析出视图函数但是并未执行该视图函数时
        print("process_view(FirstMiddleware)......,view=",view,'args=',args,'kwargs=',kwargs)


    def process_response(self, request, response):   #  接收到响应时，自动执行该方法
        print("process_response(FirstMiddleware)......")
        return response    #  一定要返回该响应对象


    def process_exception(self, request, exception):    #  发生异常时，并且未处理该异常，自动执行该方法
        print("process_exception(FirstMiddleware)......,exception=",exception)



class SecondMiddleware(MiddlewareMixin):
    def process_request(self, request):  # 每次接收到请求时，自动执行该方法
        print("process_request(SecondMiddleware)......")


    def process_response(self, request, response):   #  接收到响应时，自动执行该方法
        print("process_response(SecondMiddleware)......")
        return response    #  一定要返回该响应对象


r = redis.Redis(host='localhost',port=6379,db=3)   # 操作Redis的实例化对象


class LimitMiddleware(MiddlewareMixin):    #  自定义限速中间件

    def process_request(self,request):    # 一接收到请求，就会执行该方法
        ip = request.META.get("REMOTE_ADDR")   # 获取发送请求的客户端的IP地址
        key = "limit:" + ip
        is_ok = r.set(key,1,ex=60,nx=True)   #  当key不存在时，set命令才能执行成功
        print("is_ok=",is_ok)
        if is_ok or r.incr(key) <= 5:    #  是第一次访问，或者访问次数未超过5次
            request.visit_count = r.get(key).decode()      #  给request对象动态添加一个visit_count属性
        else:
            return HttpResponse("<h3 style='color:red'>您的访问过于频繁，请稍后再访问！</h3>")






