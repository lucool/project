import random

from flask import g


def load_middleware(app):

    @app.before_first_request
    def a():
        print("第一次请求before_first_request......")

    @app.before_request
    def b():  # 每次请求都要执行该方法
        print("before_request......")
        number = random.randint(1,100)
        if number >= 80:
            g.data = "三十六计"
            return "<h3>恭喜，中奖了，后面不用访问了，生成的随机数是：" + str(number) + "</h3>"

        g.data = "孙子兵法"  # 给g对象动态添加一个data属性

    @app.after_request
    def c(response):
        print("after_request...g.data=",g.data)
        return response    # 这里一定要返回响应对象！

    @app.teardown_request
    def d(e):
        print("teardown_request......e=",e)


