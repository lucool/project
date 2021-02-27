from datetime import timedelta

import redis
from flask import Flask
from flask_session import Session

from CookieSessionApp.views import blue1,blue2


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abcdef"  # 设置session秘钥
    app.config["SESSION_TYPE"] = "redis"  # 设置session存储的位置
    app.config["SESSION_REDIS"] = redis.Redis(host="localhost",port=6379,db=0)  # 设置操作Redis的对象
    app.config["SESSION_KEY_PREFIX"] = "python1904"   # session前缀
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(seconds=30)  #  最大不交互时间
    app.register_blueprint(blue1)   # 程序实例注册关联蓝图对象
    app.register_blueprint(blue2)
    Session(app)   # Flask-Session插件中的Session对象与程序实例关联
    return app