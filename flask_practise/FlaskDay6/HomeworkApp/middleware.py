from flask import request, session, flash, redirect, url_for

REQUIRED_PATH = ["/success/"]

def load_middleware(app):

    @app.before_request
    def check():
        path = request.path   # 获取当前访问的路由
        if path in REQUIRED_PATH:   # 判断是否是需要登录验证的路径
            username = session.get("username")
            if not username:
                flash("您还未登录，不能访问成功页面，请先登录！")
                return redirect(url_for("myblue.login_view"))  # 重定向到登录页面
