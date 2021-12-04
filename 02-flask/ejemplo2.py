from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def portada():
    titulo = 'Inicio'
    return render_template('portada.html', title=titulo)


@app.route("/hola")
def hola():
    valores = {'nombre': 'José', 'edad': 34, 'color': 'Negro'}
    return render_template('hola.html', datos=valores)


@app.route('/colores')
def colores():
    colores = ['negro', 'gris', 'amarillo', 'azul', 'rojo']
    return render_template('colores.html', colores=colores)


@app.route('/frase/<texto>')
def frase(texto):
    return render_template('frase.html', tipo=texto)


if __name__ == '__main__':
    app.run(debug=True)
