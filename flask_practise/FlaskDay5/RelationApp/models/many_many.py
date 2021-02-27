from RelationApp.ext import db

# 设置中间表
mem_com = db.Table("member_community",
                   db.Column("member_id",db.Integer,db.ForeignKey("members.id"),primary_key=True),
                   db.Column("community_id",db.Integer,db.ForeignKey("communities.id"),primary_key=True)
          )


class Member(db.Model):    #  成员模型
    __tablename__ = "members"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    age = db.Column(db.Integer)


class Community(db.Model):   # 社团模型
    __tablename__ = "communities"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    slogon = db.Column(db.String(20))
    mems = db.relationship("Member",secondary=mem_com,backref="comms")  # 关联另一个多方模型和中间表对象
