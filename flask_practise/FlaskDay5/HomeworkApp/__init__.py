from flask import Flask
print("2222222")
from HomeworkApp.ext import init_ext
from HomeworkApp.views import blue


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/mydb?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    init_ext(app)
    app.register_blueprint(blue)
    return app