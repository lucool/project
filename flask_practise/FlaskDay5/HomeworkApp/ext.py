from flask_sqlalchemy import SQLAlchemy
print("333333333")
db = SQLAlchemy()
print("444444444",id(db))

def init_ext(app):
    db.init_app(app)