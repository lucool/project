from flask import Blueprint, request

blue = Blueprint("myblue",__name__)


@blue.route("/food/")
def food_view():
    food_name = request.args.get("name","默认食物")   #  接收查询字符串参数(以？将URL与参数隔开)
    return "<h3>接收到的食物是：<span style='color:blue'>" + food_name + "</span></h3>"


@blue.route("/user/",methods=["GET","POST"])
def user_view():
    username = request.form.get("username","默认用户名")   # 接收封装到请求体(body)中的username参数
    password = request.form.get("password","默认密码")  # 接收封装到请求体(body)中的password参数
    return "用户名是：" + username +"；密码是：" + password


