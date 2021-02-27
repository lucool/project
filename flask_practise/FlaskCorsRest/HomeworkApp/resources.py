from flask_restful import Resource, fields, marshal
from flask_restful.reqparse import RequestParser

from HomeworkApp.models import Fruit


req_parser = RequestParser()
req_parser.add_argument("fruit_id",required=True)

fruit_instance = {
    "fruit_id":fields.Integer(attribute="id"),
    "fruit_name":fields.String(attribute="name"),
    "fruit_price":fields.Float(attribute="price")
}

fruit_output = {
    "code":fields.String,
    "msg":fields.String,
    "fruit":fields.Nested(fruit_instance)
}

fruit_notfound = {
    "code":fields.String,
    "msg":fields.String
}


class FruitResource(Resource):
    def get(self):
        args = req_parser.parse_args()
        fruit_id = args.get("fruit_id")
        fruit = Fruit.query.get(fruit_id)
        if fruit:
            data = {
                "code":"200",
                "msg":"恭喜，水果查到了~~~",
                "fruit":fruit
            }
            return marshal(data,fruit_output)
        else:
            data = {
                "code":"404",
                "msg":"sorry,暂无此水果信息！"
            }
            return marshal(data,fruit_notfound)