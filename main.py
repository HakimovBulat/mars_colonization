from flask import Flask, url_for, request


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
                    <h1 id="wait_mars">Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" alt="здесь должна была быть картинка, но не нашлась"> 
                    <div class="alert alert-primary" role="alert"> Как гласит народная мудрость:</div>
                    <div class="alert alert-secondary" role="alert"> Одна планета - хорошо, но две - лучше!</div>
                    <div class="alert alert-success" role="alert"> Так давайте начнём с Марса! </div>
                    <div class="alert alert-warning" role="alert"> Присоединяйся! </div>
                  </body>
                </html>"""

@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента на участие в суперсекретной миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Основное общее</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>

                                    <div class="form-group">
                                        <label for="form-check">Кем вы работаете?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="education" id="doctor" value="doctor">
                                          <label class="form-check-label" for="doctor">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="education" id="teacher" value="teacher">
                                          <label class="form-check-label" for="teacher">
                                            Учитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="education" id="builder" value="builder">
                                          <label class="form-check-label" for="builder">
                                            Строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="education" id="pilot" value="pilot">
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>

                                    <div class="form-group">
                                        <label for="motivation">Почему вы хотите принять участие в мисси?</label>
                                        <textarea class="form-control" id="motivation" rows="3" name="motivation"></textarea>
                                    </div>

                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form.get('surname'))
        print(request.form.get('name'))
        print(request.form.get('email'))
        print(request.form.get('education'))
        print(request.form.get('profession'))
        print(request.form.get('motivation'))
        print(request.form.get('sex'))
        print(request.form.get('accept'))
        return "Форма отправлена"

@app.route('/choice/<planet_name>')
def choice(planet_name):
    planets = {'меркурий': ['Здесь очень жарко', 'День круглые сутки'], 
               'земля': ['Мы уже привыкли здесь жить', 'Здесь есть жизнь'], 
               'марс': ['Есть атмосфера', 'Существует магнитное поле'], 
               'венера': ['Очень красивая планета', 'Доволно-таки тепло'], 
               'уран': ['Холодновато', 'Зато не нужен кондиционер'], 
               'нептун': ['Самая далёкая планета от солцна', 'Не нужны противосолнечные очки'], 
               'сатурн': ['Есть интересные кольца', 'Состоит из газа'],
               'юпитер': ['Самая большая планета в солнечной системе', 'Имеет интересный окрас']
               }
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Моё предложение: {planet_name}</h1>
                    <div class="alert alert-secondary" role="alert"> {planets[planet_name][0]}</div>
                    <div class="alert alert-success" role="alert"> {planets[planet_name][1]} </div>
                  </body>
                </html>'''

@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''<!doctype htnl>
              <html>
                <head>
                    <meta charset="utf-8">
                    <title>Результаты</title>
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                </head>
                <body>
                    <h1>Результаты отбора</h1>
                    <div class="alert alert-primary" role="alert">Претендента на участие в миссии {nickname}:</div>
                    <div class="alert alert-success" role="alert">Ваш рейтинг после {level} этапа отбора</div>
                    <div class="'alert alert-info" role="alert">Составляет {rating}!</div>
                    <div class="alert alert-danger" role="alert">Поздравляем и желаем удачи!</div>
                </body>
            </html>'''


@app.route('/carousel')
def carousel():
    return f'''<!doctype htnl>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Результаты</title>
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                </head>
                <body>
                <h1>Пейзажи марса</h1>
                  <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
                  <div class="carousel-inner">
                    <div class="carousel-item active">
                      <img class="d-block w-100" src="{url_for('static', filename='img/landscape1.jpg')}" alt="First slide">
                    </div>
                    <div class="carousel-item">
                      <img class="d-block w-100" src="{url_for('static', filename='img/landscape2.jpg')}" alt="Second slide">
                    </div>
                    <div class="carousel-item">
                      <img class="d-block w-100" src="{url_for('static', filename='img/landscape3.jpg')}" alt="Third slide">
                    </div>
                  </div>
                </div>
                </body>
            </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')