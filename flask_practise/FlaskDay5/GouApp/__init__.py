from flask import Flask

from GouApp.middleware import load_middleware
from GouApp.views import blue


def create_app():
    app = Flask(__name__)
    load_middleware(app)
    app.register_blueprint(blue)
    return app