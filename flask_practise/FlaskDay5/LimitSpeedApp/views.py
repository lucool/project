from flask import Blueprint, g

blue = Blueprint("myblue",__name__)


@blue.route("/index/")
def index_view():
    count = g.visit_count
    return "<h3>恭喜，这是第<span style='color:pink'>" + str(count) + "</span>次访问</h3>"