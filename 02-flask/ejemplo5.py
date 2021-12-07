from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField,  # DataTimeField,
                     RadioField, SelectField, TextAreaField,
                     SubmitField)  # TextField,

from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JOSER2087'


class Formulario(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    edad = BooleanField('Eres mayor de edad ?')
    sexo = RadioField('sexo', choices=[('h', 'hombre'), ('m', 'mujer')])
    color = SelectField('Color Favorito', choices=[('r', 'rojo'), ('n', 'negro')])
    comentario = TextAreaField()
    boton = SubmitField('Enviar')


@app.route('/informacion')
def informacion():
    render_template('informacion.html')


@app.route('/datos', methods=['GET', 'POST'])
def datos():
    formulario = Formulario()
    if formulario.validate_on_submit():
        session['nombre'] = formulario.nombre.data
        session['edad'] = formulario.edad.data
        session['sexo'] = formulario.sexo.data
        session['color'] = formulario.color.data
        session['comentario'] = formulario.comentario.data
        return redirect(url_for('informacion'))

    return render_template('datos.html', formulario=formulario)


if __name__ == '__main__':
    app.run(debug=True)
