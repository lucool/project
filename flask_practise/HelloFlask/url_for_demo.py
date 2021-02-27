from flask import Flask, redirect, url_for
from flask_script import Manager

app = Flask(__name__)   #  创建Flask程序实例对象
manager = Manager(app)


@app.route("/hello/<stuname>/")
def hello_view(stuname):
    new_url = url_for("welcome_view",name=stuname)   # 使用url_for()反向解析出路由
    print("url_for()反向解析出的路由是：",new_url)
    return redirect(new_url)   #  发起重定向动作


@app.route("/welcome/<name>/")
def welcome_view(name):
    return "<h3>欢迎你，<span style='color:blue'>" + name + "</span></h3>"


if __name__ == '__main__':
    manager.run()