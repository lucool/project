from SQLAlchemyApp.ext import db


class Cake(db.Model):     # 创建Cake模型类
    __tablename__ = "cakes"   #  模型映射的数据库表名称
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)  # 映射表中的自增主键
    name = db.Column(db.String(20),nullable=False)
    price = db.Column(db.Float,nullable=False)


class Product(db.Model):    #  创建Product模型类
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 映射表中的自增主键
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    brand = db.Column(db.String(20),nullable=False)
    numbers = db.Column(db.Integer,nullable=False)
