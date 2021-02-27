from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   # 实例化SQLAlchemy对象，该对象用来操作SQLAlchemy工具集

def init_ext(app):
    db.init_app(app)   # 将SQLAlchemy对象与Flask程序实例关联