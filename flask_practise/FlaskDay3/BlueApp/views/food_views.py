from flask import Blueprint

blue2 = Blueprint("food_blue",__name__)


@blue2.route("/noodles/")
def noodles_view():
    return "<h3 style='color:pink'>吃面条......</h3>"


@blue2.route("/rice/")
def rice_view():
    return "<h3 style='color:yellow'>米饭真香......</h3>"