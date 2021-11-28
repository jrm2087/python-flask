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
    return f'posicion 5 del nombre es {nombre[5]}'
    # return f'<h2>hola {nombre}, buenos dias</h2>'


@app.route('/longitud/<palabra>')
def logintud(palabra):
    return f'La longitud de la palabra "{palabra}" es: {len(palabra)}'


@app.route('/edad/<nombre>/<edad>')
def edad(nombre: str, edad):
    return f'{nombre.upper()} tiene {edad}'


@app.route('/sumar/<num1>/<num2>')
def sumar(num1, num2):
    return f'La suma de {num1} y {num2} es {int(num1) + int(num2)}'


if __name__ == '__main__':
    app.run(debug=True)
