from flask import Flask, make_response
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route("/response/")
def salary_view():
    response = make_response("<h3 style='color:blue'>省长将访问，请接待！</h3>")  # 创建响应对象
    response.headers["beautiful"] = "beautiful flowers"   # 添加响应头信息
    response.headers["Content-Type"] = "text/xml"   # 修改Content-Type,告诉客户端以何种方式显示响应体
    return response


if __name__ == '__main__':
    manager.run()