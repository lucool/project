from flask import Flask

from ParamApp.views import blue


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blue)   # 注册蓝图
    return app