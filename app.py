from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/player/<int:nid>')
def player(nid):
    id = nid * 2
    return f'当前请求的动态参数为：{id}'


if __name__ == '__main__':
    app.run()
