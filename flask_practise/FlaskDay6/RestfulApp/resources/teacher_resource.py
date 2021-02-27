from flask_restful import Resource, fields, marshal_with
from flask_restful.reqparse import RequestParser

from RestfulApp.ext import db
from RestfulApp.models import Teacher

req1 = RequestParser()    #  创建RequestParser请求解析器对象
req1.add_argument("name",type=str,required=True,help="必须传递name参数，并且为字符串类型！")
req1.add_argument("age",type=int,help="年龄必须是整数",dest="t_age")  # 前端使用age传参，后端使用t_age接收参数
req1.add_argument("salary",type=float,required=True,help="必须传递salary参数，并且为小数！")

# 老师实例化对象定制输出模板
teacher_instance = {
    "teacher_id":fields.Integer(attribute="id"),
    "teacher_name":fields.String(attribute="name"),
    "teacher_age":fields.Integer(attribute="age"),
    "teacher_salary":fields.Float(attribute="salary"),
}

teacher_output = {
    "code":fields.String,
    "msg":fields.String,
    "teacher":fields.Nested(teacher_instance,attribute="new_teacher")
}


class TeacherResource(Resource):
    @marshal_with(teacher_output)
    def post(self):
        print("111111111111111")
        args = req1.parse_args()   #  解析参数,并且校验数据
        print("222222222222222")
        name = args.get("name")   # 获取参数名为name的参数值
        age = args.get("t_age")  # 使用t_age接收参数，因为add_argument()中的dest指定了
        salary = args.get("salary")  # 获取参数名为salary的参数值
        new_teacher = Teacher(name=name,age=age,salary=salary)
        db.session.add(new_teacher)
        db.session.commit()
        data = {
            "code":"666",
            "msg":"老师添加成功~",
            "new_teacher":new_teacher
        }
        return data
