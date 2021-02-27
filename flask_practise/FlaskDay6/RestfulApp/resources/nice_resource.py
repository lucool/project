from flask_restful import Resource, marshal, fields
from flask_restful.reqparse import RequestParser

req = RequestParser()
req.add_argument("hobby",action="append")   # 接收多个同名参数
req.add_argument("User-Agent",location="headers",dest="ua")  #  接收请求头信息名称为User-Agent的值
req.add_argument("csrftoken",location="cookies",dest="cf")  #  接收Cookie名称为csrftoken的值



nice_output = {
    "code":fields.String,
    "msg":fields.String,
    "hobby":fields.List(fields.String),
    "user-agent":fields.String,
    "csrftoken":fields.String
}


class NiceResource(Resource):

    def get(self):
        args = req.parse_args()
        hobby_data = args.get("hobby")
        print("hobby_data=",hobby_data," type:",type(hobby_data))
        user_agent = args.get("ua")
        cf = args.get("cf")
        data = {
            "code":"666",
            "msg":"恭喜获取数据~~",
            "hobby":hobby_data,
            "user-agent":user_agent,
            "csrftoken":cf
        }
        return marshal(data,nice_output)
