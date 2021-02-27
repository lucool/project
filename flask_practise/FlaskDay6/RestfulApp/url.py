from flask_restful import Api

from RestfulApp.resources.nice_resource import NiceResource
from RestfulApp.resources.teacher_resource import TeacherResource
from RestfulApp.resources.toy_resource import ToyResource, ManyToyResource

api = Api()


def init_api(app):
    api.init_app(app)   # Api与Flask程序实例进行关联


api.add_resource(ToyResource,"/toy/","/toy/<int:toy_id>/")   # 关联资源类与接口路由

api.add_resource(ManyToyResource,"/toys/")

api.add_resource(TeacherResource,"/teacher/")

api.add_resource(NiceResource,"/nice/")