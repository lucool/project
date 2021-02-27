from RestfulApp.ext import db


class Toy(db.Model):   # 玩具模型
    __tablename__ = "toys"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    color = db.Column(db.String(20))


class Teacher(db.Model):   # 老师模型
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer)
    salary = db.Column(db.Float,nullable=False)
