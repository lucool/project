from flask import Blueprint

blue1 = Blueprint("sport_blue",__name__)  #  创建蓝图对象，并传入蓝图名称和导入名称


@blue1.route("/jog/")
def jog_view():
    return "<h3 style='color:blue'>慢跑中......</h3>"


@blue1.route("/swim/")
def swim_view():
    return "<h3 style='color:green'>游泳~~~</h3>"