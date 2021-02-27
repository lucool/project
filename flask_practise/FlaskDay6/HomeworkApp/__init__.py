from flask import Flask

# 缓存配置
from HomeworkApp.ext import init_ext
from HomeworkApp.middleware import load_middleware
from HomeworkApp.views import c, blue

cache_config = {
    "CACHE_TYPE":"redis",
    "CACHE_REDIS_HOST":"localhost",
    "CACHE_REDIS_PORT":6379,
    "CACHE_REDIS_DB":3
}


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abcdef"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/mydb?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    init_ext(app)
    c.init_app(app,config=cache_config)   # Cache对象关联程序实例app,与缓存配置
    app.register_blueprint(blue)
    load_middleware(app)
    return app