import time
from flask import Blueprint
from flask_cache import Cache

blue = Blueprint("myblue",__name__)
c = Cache()

count = 0


@blue.route("/index/")
@c.cached(timeout=30,key_prefix="python1904")   # 先使用cached装饰器
def index_view():
    print("模拟耗时操作......")
    time.sleep(3)
    global count
    count += 1
    return "<h3>第" + str(count) + "次进入index_view()视图函数......</h3>"

