from flask import Flask


app = Flask(__name__)


@app.route('/')
@app.route('/name_mission')
def name_mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    promotion_list = ["Как гласит народная мудрость:", 'Одна планета - хорошо, но две - лучше!',
                      "Так давайте начнём с Марса!", "Присоединяйся!"
                      ]
    return '<br>'.join(promotion_list)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')