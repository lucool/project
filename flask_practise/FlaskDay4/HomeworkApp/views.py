from flask import Blueprint, render_template, request

from HomeworkApp.db.tools import select_fruits,select_single_fruit

blue = Blueprint("fruit_blue",__name__)


@blue.route("/fruits/")
def fruits_view():
    fruits = select_fruits()
    return render_template("fruit/fruits.html",fruits=fruits)


@blue.route("/fruit/")
def fruit_detail_view():
    id = request.args.get("id")   # 接收查询字符串参数
    fruit = select_single_fruit(id)
    return render_template("fruit/detail_fruit.html",fruit=fruit)