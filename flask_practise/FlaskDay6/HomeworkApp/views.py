import time

from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from flask_cache import Cache
from HomeworkApp.models import Student, User

blue = Blueprint("myblue",__name__)

c = Cache()


@blue.route("/student/<int:sid>/")
@c.cached(timeout=30)
def stuedent(sid):
    print("查询MySQL数据库......")
    time.sleep(3)
    student = Student.query.get(sid)
    if student:
        return render_template("student.html",student=student)
    else:
        return "<h3 style='color:red'>无此学生的信息！</h3>"


@blue.route("/login/",methods=["GET","POST"])
def login_view():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        logname = request.form.get("logname")
        logpwd = request.form.get("logpwd")
        user = User.query.filter_by(username=logname,password=logpwd).first()
        print("user=",user)
        if user:
            session["username"] = logname   # 验证成功后，设置会话属性
            return redirect(url_for("myblue.success_view"))   # 重定向到成功页面
        else:
            flash("用户名或密码错误，请重新登录！")
            return redirect(url_for("myblue.login_view"))   # 重定向到登录页面


@blue.route("/success/")
def success_view():
    return render_template("success.html")

