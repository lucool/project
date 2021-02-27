from flask import Flask

from Innerobject_App.views import blue


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blue)
    app.config["HERO"] = "曼施坦因"
    return app