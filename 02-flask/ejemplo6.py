from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jrm2087'


class Formulario(FlaskForm):
    nombre = StringField('Nombre')
    boton = SubmitField('Enviar mensaje')


@app.route('/mensaje', methods=['GET', 'POST'])
def mensaje():
    formulario = Formulario()
    if formulario.validate_on_submit():
        nombre = formulario.nombre.data
        flash(f'hola {nombre}, Gracias por pulsar este boton')
        return redirect(url_for('mensaje'))
    return render_template('mensaje.html', formulario=formulario)


if __name__ == '__main__':
    app.run(debug=True)
