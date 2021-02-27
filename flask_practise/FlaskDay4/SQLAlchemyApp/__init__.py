from flask import Flask

from SQLAlchemyApp.ext import init_ext


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/mydb?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # 不记录操作日志
    init_ext(app)
    return app