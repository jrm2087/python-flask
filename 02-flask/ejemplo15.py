import os
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
directorio = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio, 'personas_api.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

api = Api(app)


class PersonaBD(db.Model):
    nombre = db.Column(db.String(100), primary_key=True)

    def __init__(self, nombre):
        self.nombre = nombre

    def json(self):
        return {'name': self.nombre}


class Personas(Resource):
    def get(self, valor):
        persona = PersonaBD.query.filter_by(nombre=valor).first()
        if persona:
            return persona.json()
        return {'resultado': 'No se encontro registro.'}

    def post(self, valor):
        persona = PersonaBD(nombre=valor)
        db.session.add(persona)
        db.session.commit()
        return {'respuesta': 'persona añadida correctamente'}

    def delete(self, valor):
        persona = PersonaBD.query.filter_by(nombre=valor).first()
        db.session.delete(persona)
        db.session.commit()
        return {'resultado': 'Persona borrada correctamente.'}


class Listar(Resource):
    def get(self):
        personas = PersonaBD.query.all()
        lista_persona = [p.json() for p in personas]
        return {'resultado': lista_persona}


api.add_resource(Personas, '/persona/<string:valor>')
api.add_resource(Listar, '/listar/')

if __name__ == '__main__':
    app.run(debug=True)
