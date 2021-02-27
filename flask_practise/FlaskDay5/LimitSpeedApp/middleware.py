import redis
from flask import request, g

r = redis.Redis(host='localhost',port=6379,db=3)   # 操作Redis的实例对象

def load_middleware(app):

    @app.before_request
    def check_speed():
        ip = request.remote_addr    #  获取客户端的IP地址
        key = "limit:" + ip
        # 将客户端IP作为key,访问次数作为value,过期时间为60秒，只有在该key不存在的情况下set命令才会真正执行
        is_ok = r.set(key,1,ex=60,nx=True)  # 返回的is_ok用来判断set命令是否在redis中真正执行了
        print("is_ok=",is_ok)
        if is_ok or r.incr(key) <= 5:   # 1分钟内的第一次访问或者访问次数未超过5次，均可放行
            g.visit_count = r.get(key).decode()   # 将访问次数设置到g对象中
        else:
            return "<h3 style='color:red'>访问过于频繁，请稍后再访问！</h3>"

