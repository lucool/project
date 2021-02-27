from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()   # 用来操作关系型数据库的对象

def init_ext(app):
    db.init_app(app)