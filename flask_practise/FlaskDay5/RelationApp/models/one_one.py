from RelationApp.ext import db


class Person(db.Model):   # 人"一方"
    __tablename__ = "person"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    card = db.relationship("Card",backref="per",uselist=False)   # 禁用列表


class Card(db.Model):   # 卡"一方"(依赖一方)
    __tablename__ = "cards"
    cardno = db.Column(db.String(20), primary_key=True)
    color = db.Column(db.String(20),nullable=False)
    person_id = db.Column(db.Integer,db.ForeignKey("person.id"),unique=True)  # 唯一外键

