from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')


@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')


@app.route('/formulario')
def formulario():
    return render_template('formulario.html')


@app.route('/gracias')
def gracias():
    valor1 = request.args.get('nombre')
    valor2 = request.args.get('apellidos')
    return render_template('gracias.html', nombre=valor1, apellidos=valor2)


@app.route('/nombre')
def nombre():
    return render_template('nombre.html')


@app.route('/resultado')
def resultado():
    nombre = request.args.get('nombre')
    minuscula = any(letra.islower() for letra in nombre)
    numero = any(letra.isdigit() for letra in nombre)
    mayuscula = nombre[0].isupper()
    resul = minuscula and numero and mayuscula
    return render_template('resultado.html', resul=resul, minuscula=minuscula, mayuscula=mayuscula, numero=numero)


@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('pagina404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
