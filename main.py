from flask import Flask


app = Flask(__name__)


print(9)
@app.route('/')
@app.route('/name_mission')
def name_mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')