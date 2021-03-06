from flask import Flask  # это подключние библиотечки Flask, чтобы с ней работать можно было

# создаем экземпляр веб приложения (да-да веб приложение — это просто экземпляр класса)
# __name__ -- это просто имя нашего файла, чтобы можно было отличить одно приложение от другого
# если их вдруг будет несколько
app = Flask(__name__)  

@app.route('/') # путь на который мы будем реагировать, пока не будем вникать почему надо писать именно так 
def hello(): # объявляем обычную функцию, с именем hello
    return 'Привет! =)' # возвращаем ответ на запрос в виде фразы "Привет!"

@app.route('/123')
def my_new_url_with_123():
    return('И снова здравствуй, так и что не меняемся?')

@app.route('/hello/')
@app.route('/hello/<name>')
def new_hello(name="странник"):
    return f'Привет, {name}'

@app.route('/bye/')
@app.route('/bye/<name>')
def goodbye(name="Я не знаю с кем прощаться, поэтому и не буду"):
    if " " in name:
        return f'Хорошего Вам дня, {name}'
    if "" in name:
        return f'Пока, {name}'
    else:
        return f'{name}'



@app.route('/plus/<int:a>/<int:b>')
def plus(a, b):
    return f"Сумма {a} + {b} = {a + b}"

@app.route('/sub/<int:a>/<int:b>')
def sub(a, b):
    return f"Разность {a} - {b} = {a - b}"

@app.route('/mul/<int:a>/<int:b>')
def mul(a, b):
    return f"{a} * {b} = {a * b}"

@app.route('/div/<int:a>/<int:b>')
def div(a, b):
    return f"{a} / {b} = {a / b}"



@app.route('/<int:a>/<operation>/<int:b>')
def operate(operation, a, b):
    if "плюс" in operation:
        return f"{a + b}"
    if "минус" in operation:
        return f"{a - b}"
    if "умножить" in operation:
        return f"{a * b}"
    if "разделить" in operation:
        return f"{a / b}"