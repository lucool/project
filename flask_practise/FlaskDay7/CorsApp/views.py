from flask import Blueprint, jsonify

blue = Blueprint("cors_blue",__name__)


@blue.route("/nice/")
def nice_view():
    data = {
        "msg":"恭喜，跨域请求成功了~~~"
    }
    return jsonify(data)