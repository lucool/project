from flask import Flask
from flask_cors import CORS

from HomeworkApp.ext import init_ext
from HomeworkApp.url import init_api


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/mydb?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    CORS(app)
    init_ext(app)
    init_api(app)
    return app