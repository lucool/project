from flask_restful import Resource, fields, marshal_with, marshal
from flask_restful.reqparse import RequestParser

from HomeworkApp.ext import db
from HomeworkApp.models import School

req_school = RequestParser()
req_school.add_argument("name",required=True,help="必须传递name参数！")
req_school.add_argument("address",required=True,help="必须传递address参数！")

school_instance = {
    "school_id":fields.Integer(attribute="id"),
    "school_name":fields.String(attribute="name"),
    "school_address":fields.String(attribute="address")
}

school_output = {
    "code":fields.String,
    "msg":fields.String,
    "school":fields.Nested(school_instance)
}

notfound_output = {
    "code":fields.String,
    "msg":fields.String
}


class SchoolResource(Resource):
    @marshal_with(school_output)
    def post(self):
        args = req_school.parse_args()  # 解析参数，校验数据
        school_name = args.get("name")
        school_address = args.get("address")
        new_school = School(name=school_name,address=school_address)
        db.session.add(new_school)
        db.session.commit()
        data = {
            "code":"666",
            "msg":"新学校添加完毕！",
            "school":new_school
        }
        return data

    def get(self,schid):
        school = School.query.get(schid)
        if school:
            data = {
                "code":"200",
                "msg":"查到了~~",
                "school":school
            }
            return marshal(data,school_output)
        else:
            data = {
                "code": "404",
                "msg": "无该校信息！",
            }
            return marshal(data, notfound_output)
