from flask import Flask, url_for


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


@app.route('/image_mars')
def image():
    return f'''<title>Привет, Марс!</title> <h1>Жди нас, Марс!</h1> <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась"> <p>Вот он - красивый марс<p>'''

@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" alt="здесь должна была быть картинка, но не нашлась"> 
                    <div class="alert alert-primary" role="alert"> Как гласит народная мудрость:</div>
                    <div class="alert alert-secondary" role="alert"> Одна планета - хорошо, но две - лучше!</div>
                    <div class="alert alert-success" role="alert"> Так давайте начнём с Марса! </div>
                    <div class="alert alert-warning" role="alert"> Присоединяйся! </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')