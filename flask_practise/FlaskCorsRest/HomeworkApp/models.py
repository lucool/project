from HomeworkApp.ext import db


class Fruit(db.Model):
    __tablename__ = "fruits"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    price = db.Column(db.Float,nullable=False)