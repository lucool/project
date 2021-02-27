from flask import Flask, redirect
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route("/hello/")
def hello_view():
    print("hello_view()......")
    return redirect("http://www.sohu.com/")   # 重定向到“外网”


@app.route("/hi/")
def hi_view():
    print("hi_view()......")
    return redirect("/hello/")   # 重定向到本应用下的"/hello/"路由


if __name__ == '__main__':
    manager.run()