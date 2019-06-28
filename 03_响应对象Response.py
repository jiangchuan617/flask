from flask import Flask,make_response

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def hello():
    # 实际上返回的是一个Response对象，包含
    # status code 200,404,301
    # content-type 放置在 http headers属性中，如何解析返回的主体内容
    # content-type=text/html 默认
    '''
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html></html>', 404)
    response.headers = headers
    return response
    '''

    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.bing.com'
    }
    response = make_response('<html></html>', 301)  # 301 代表重定向
    response.headers = headers
    # return response
    '''
    如果是接受app的信息（一般是json格式）
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.bing.com'
    }
    '''

    # 也可以不用make_response,直接返回元组
    return '<html></html>', 301, headers



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=app.config['DEBUG'])