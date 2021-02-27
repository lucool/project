from flask import Flask

from BlueApp.views import blue1,blue2


def create_app():
    app = Flask(__name__)   # 创建Flask程序实例
    app.register_blueprint(blue1)   # app程序实例注册blue1蓝图对象
    app.register_blueprint(blue2)   # app程序实例注册blue2蓝图对象
    return app