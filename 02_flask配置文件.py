from flask import Flask

app = Flask(__name__)
app.config.from_object('config')  # 载入配置文件
# print(type(app.config))  # app.config 是字典类型的子类
# 通过app.config.from_object()导入的变量必须是大写'DEBUG'
# 'DEBUG'在flask内是一个默认参数,值为False，即使config.py中没有DEBUG,app.config['DEBUG'依旧能读取到

@app.route("/hello/")
def hello():
    return "<h1 style='color:red'> hello world~!</h1>"



if __name__ == "__main__":
    # 生产环境下 nginx+uwsgi部署,不用flask自带的服务器
    app.run(host="0.0.0.0", debug=app.config['DEBUG'])
