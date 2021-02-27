from flask import request
from flask_restful import Resource, marshal_with, fields, marshal

from RestfulApp.ext import db
from RestfulApp.models import Toy

# Toy实例化对象定制输出模板
toy_instance = {
    "toy_id":fields.Integer(attribute="id"),
    "toy_name":fields.String(attribute="name"),
    "toy_color":fields.String(attribute="color")
}

# post定制输出模板
toy_output = {
    "code":fields.String,
    "msg":fields.String,
    "new_toy":fields.Nested(toy_instance)
}

# get获取单个玩具输出模板
toy_output2 = {
    "code":fields.String,
    "msg":fields.String,
    "toy":fields.Nested(toy_instance)
}


class ToyResource(Resource):   # 自定义玩具资源类

    @marshal_with(toy_output)
    def post(self):   # 实现post分派方法
        toy_name = request.form.get("toy_name")   # 接收请求体中的toy_name参数
        toy_color = request.form.get("toy_color")   # 接收请求体中的toy_color参数
        new_toy = Toy(name=toy_name,color=toy_color)
        db.session.add(new_toy)
        db.session.commit()  # 将新数据提交到数据库表中
        data = {
            "code":"666",
            "msg":"新玩具添加成功！",
            "new_toy":new_toy
        }
        return data

    def get(self,toy_id):
        toy = Toy.query.get(toy_id)
        if toy:
            data = {
                "code":"678",
                "msg":"查询成功",
                "toy":toy
            }
            return marshal(data,toy_output2)  # 通过marshal()函数将原始数据与输出模板对应起来
        else:
            data = {
                "code":"404",
                "msg":"没有该玩具"
            }
            not_found_output = {
                "code":fields.String,
                "msg":fields.String
            }
            return marshal(data,not_found_output)

toys_output = {
    "code":fields.String,
    "msg":fields.String,
    #"toys":fields.Nested(toy_instance)
    "toys":fields.List(fields.Nested(toy_instance))
}


class ManyToyResource(Resource):

    def get(self):
        toys = Toy.query.all()
        data = {
            "code": "678",
            "msg": "查询所有成功",
            "toys": toys
        }
        return marshal(data,toys_output)
