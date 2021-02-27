from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

LOGIN_REQUIRED_URL = ["/home/success/"]  # 需要进行登录验证的路由列表

class MyMiddleware(MiddlewareMixin):

    def process_request(self,request):
        print("request.path=",request.path)
        if request.path in LOGIN_REQUIRED_URL:
            if not request.session.get("username"):  # 如果没有登录
                request.session["msg"] = "您还未登录，请先登录！"  # 在session中暂存消息
                return redirect(reverse("home:log"))   # 重定向到登录页面