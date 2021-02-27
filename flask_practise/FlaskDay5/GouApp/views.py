from flask import Blueprint, g

blue = Blueprint("myblue",__name__)


@blue.route("/index/")
def index_view():
    print("进入视图函数index_view了,g.data=",g.data)
    try:
        5 / 0
    except Exception as e:
        print("异常被捕获了~~~")
    return "index~~~"