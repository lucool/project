print("666666")
from HomeworkApp.ext import db
print("7777777")

class School(db.Model):   #  "一方"模型
    __tablename__ = "schools"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    address = db.Column(db.String(30),nullable=False)
    students = db.relationship("Student",backref="sch")


class Student(db.Model):   # “多方”模型
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Float,nullable=False)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)  # 外键