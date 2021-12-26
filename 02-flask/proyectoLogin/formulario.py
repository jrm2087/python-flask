from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from proyectoLogin.modelos import Usuario


class FormularioRegistro(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('password_repetir', message='Contraseñas diferentes')])
    password_repetir = PasswordField('Repetir Password', validators=[DataRequired()])
    boton = SubmitField('Registrar')

    def verificar_mail(self, parametro):
        if Usuario.query.filter_by(email=parametro.data).first():
            raise ValidationError('Error, este mail ya ha sido utilizado')

    def verificar_nombre(self, parametro):
        if Usuario.query.filter_by(nombre=parametro.data).first():
            raise ValidationError('Error, este nombre ya ha sido utilizado')


class FormularioLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    boton = SubmitField('Entrar')
