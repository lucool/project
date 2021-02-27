from flask import Blueprint, g, redirect, url_for, current_app, render_template

blue = Blueprint("myblue",__name__)


@blue.route("/index/")
def index_view():
    print("index_view()......")
    g.data = "孙子兵法"
    welcome_view()
    return "index~~~"


@blue.route("/hello/")
def hello_view():
    print("hello_view()......")
    g.data = "心经"
    return redirect(url_for("myblue.welcome_view"))


@blue.route("/welcome/")
def welcome_view():
    try:
        print("welcome_view()......,g.data=",g.data)
    except Exception as e:
        print("g.data发生异常了......",e)
    return "welcome~~~"


@blue.route("/allconfig/")
def all_config_view():
    html = ""
    cf = current_app.config   #  在代码中获取程序实例的配置对象
    for k,v in cf.items():
        html += k
        html += "============>"
        html += str(v)
        html += "<br/>"
    return html


@blue.route("/show/")
def show_view():
    return render_template("show_configs.html")


