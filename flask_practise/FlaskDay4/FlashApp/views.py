from flask import Blueprint, request, render_template, redirect, url_for, session, flash

blue = Blueprint("myblue",__name__)


@blue.route("/login/",methods=["GET","POST"])
def login_view():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        logname = request.form.get("logname")
        logpwd = request.form.get("logpwd")
        if logname == "tom" and logpwd == "123456":
            session["username"] = "tom"    # 设置session属性
            return redirect(url_for("myblue.welcome_view"))
        else:
            flash("用户名或密码错误，请重新输入！")   #  将"闪消息"设置到session属性中
            flash("认真点！")
            return redirect(url_for("myblue.login_view"))   # 重定向到登录页面


@blue.route("/wel/")
def welcome_view():
    if session.get("username"):    # 判断session中是否有username属性
        return render_template("welcome.html")
    else:
        flash("您还未登录，不能直接访问欢迎页面！")
        return redirect(url_for("myblue.login_view"))   # 重定向到登录页面


@blue.route("/sessions/")
def sessions_view():
    html = ""
    for k,v in session.items():
        html += k
        html += "==========>"
        html += str(v)
        html += "<br/>"
    return html
