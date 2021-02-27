from RelationApp.ext import db


class School(db.Model):   # "一方"学校模型
    __tablename__ = "schools"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    address = db.Column(db.String(30),nullable=False)
    students = db.relationship("Student",backref="sch")  #  通过relationship()函数给多方模型类动态添加一个反向引用


class Student(db.Model):   #  "多方"学生模型
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Float,nullable=False)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)  # 从数据库角度关联“一方”模型

