from flask import Flask

app = Flask(__name__)


# 在视图函数上用装饰器做路由注册
@app.route("/hello/")  # 兼容hello/和hello
def hello():
    # 基于类的视图（即插视图）用add_url_rule
    return "<h1 style='color:red'> hello world!</h1>"


def hello2():
    return "<h1 style='color:red'> hello world~</h1>"


# 另外一种路由注册方式
app.add_url_rule('/hello2/', view_func=hello2)

if __name__ == "__main__":
    # debug=True监听程序修改
    # 可以指定本机的ip，但是不灵活
    # app.run(host='166.111.74.117',debug=True)
    app.run(host="0.0.0.0", debug=True)
