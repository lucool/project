from flask_restful import Api

from HomeworkApp.resources import FruitResource

api = Api()

def init_api(app):
    api.init_app(app)


api.add_resource(FruitResource,"/fruit/")