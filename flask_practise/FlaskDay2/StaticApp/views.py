from flask import Flask, render_template

app = Flask(__name__)   # 创建Flask程序实例


@app.route("/show/")
def show_view():
    return render_template("show_pic.html")