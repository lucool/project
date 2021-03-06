from flask import Flask

from HomeworkApp.ext import init_ext
from HomeworkApp.urls import init_api


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/mydb?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    init_ext(app)
    init_api(app)
    return app