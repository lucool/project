from flask import Flask
from flask_cors import CORS

from CorsApp.views import blue


def create_app():
    app = Flask(__name__)
    CORS(app)   # 解决跨域问题
    app.register_blueprint(blue)
    return app