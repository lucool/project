from flask import Flask, render_template

app = Flask(__name__)  # 创建Flask程序实例


@app.route("/student/<int:score>/")
def student_view(score):
    return render_template("tags/if_demo.html",score=score)   #  加载指定位置的模板，并向模板传递模板变量


@app.route("/fruits/")
def fruits_view():
    fruits = ["苹果","香蕉","橘子","菠萝","橙子"]
    return render_template("tags/for_demo.html",fruits_list=fruits)


@app.route("/child/")
def child_view():
    return render_template('extends/child.html')


@app.route("/filter/")
def filter_view():
    s = "heLLo wORLd, Haha"
    numbers = [1,2,3,4,5]
    danger = "<script>alert('大笨蛋！')</script>"
    return render_template('filter/filter_demo.html',**locals())


@app.route("/macro/")
def macro_view():
    book_list = ["红楼梦","一千零一夜","孙子兵法","水浒传"]
    return render_template("macro/call.html",books=book_list)