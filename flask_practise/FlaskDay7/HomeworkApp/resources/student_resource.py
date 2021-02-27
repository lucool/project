from flask_restful import Resource, fields, marshal_with, marshal
from flask_restful.reqparse import RequestParser

from HomeworkApp.ext import db
from HomeworkApp.models import Student

req_student = RequestParser()
req_student.add_argument("name",required=True,help="必须传递name参数！")
req_student.add_argument("score",required=True,help="必须传递score参数！")
req_student.add_argument("school_id",required=True,help="必须传递school_id参数！")


req_student2 = RequestParser()
req_student2.add_argument("id",required=True,help="必须传递学生id参数！")
req_student2.add_argument("name",required=True,help="必须传递name参数！")
req_student2.add_argument("score",required=True,help="必须传递score参数！")
req_student2.add_argument("school_id",required=True,help="必须传递school_id参数！")

student_instance = {
    "student_id":fields.Integer(attribute="id"),
    "student_name":fields.String(attribute="name"),
    "student_score":fields.Float(attribute="score"),
    "school_url":fields.String
}

student_output = {
    "code":fields.String,
    "msg":fields.String,
    "student":fields.Nested(student_instance)
}

notfound_output = {
    "code":fields.String,
    "msg":fields.String
}


class StudentResource(Resource):
    @marshal_with(student_output)
    def post(self):
        args = req_student.parse_args()
        stu_name = args.get("name")
        stu_score = args.get("score")
        school_id = args.get("school_id")
        new_student = Student(name=stu_name,score=stu_score,school_id=school_id)
        db.session.add(new_student)
        db.session.commit()
        data = {
            "code": "666",
            "msg": "新生添加完毕！",
            "student": new_student
        }
        return data

    def get(self,sid):
        student = Student.query.get(sid)
        student.school_url = "http://localhost:5000/school/" + str(student.school_id) + "/" # 动态添加school_url实例属性
        if student:
            data = {
                "code":"200",
                "msg":"查到了~~",
                "student":student
            }
            return marshal(data,student_output)
        else:
            data = {
                "code": "404",
                "msg": "无该生信息！",
            }
            return marshal(data, notfound_output)


    def put(self):
        args = req_student2.parse_args()
        id = args.get("id")
        name = args.get("name")
        score = args.get("score")
        school_id = args.get("school_id")
        stu = Student.query.get(id)
        stu.name = name
        stu.score = score
        stu.school_id = school_id
        stu.school_url = "http://localhost:5000/school/" + str(stu.school_id) + "/"  # 动态添加school_url实例属性
        db.session.commit()
        data = {
            "code":"678",
            "msg":"更新成功~~",
            "student":stu
        }
        return marshal(data,student_output)




