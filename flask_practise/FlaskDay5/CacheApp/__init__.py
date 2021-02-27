from flask import Flask
from CacheApp.views import c, blue

# 缓存配置
cache_config = {
    "CACHE_TYPE":"redis",   # 设置缓存类型为redis
    "CACHE_REDIS_HOST":"localhost",
    "CACHE_REDIS_PORT":6379,
    "CACHE_REDIS_DB":3,
}


def create_app():
    app = Flask(__name__)
    app.config.from_object(cache_config)  # 将配置设置关联到Flask程序实例
    c.init_app(app,config=cache_config)  # Cache对象与程序实例和配置信息关联
    app.register_blueprint(blue)
    return app