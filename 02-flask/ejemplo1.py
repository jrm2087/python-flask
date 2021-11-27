from flask import Flask

app = Flask(__name__)


@app.route('/')
def principal():
    return '<h1>Hola mundo</h1>'


@app.route('/salir')
def salir():
    return '<h2>Salir</h2>'


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'<h2>hola {nombre}, buenos dias</h2>'


if __name__ == '__main__':
    app.run()
