from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

personas = []


class Persona(Resource):
    def get(self, valor):
        for p in personas:
            if p == valor:
                return {'resultado': p}
        return {'resultado': 'Persona no encontrada.'}

    def post(self, valor):
        persona = valor
        personas.append(persona)
        return {'resultado': 'Persona agregada exitosamente.'}

    def delete(self, valor):
        for i, p in enumerate(personas):
            if p == valor:
                personas.pop(i)
                return {'resultado': 'Persona borrada'}


class Listar(Resource):
    def get(self):
        return {'resultado': personas}


api.add_resource(Persona, '/persona/<string:valor>')
api.add_resource(Listar, '/listar/')

if __name__ == '__main__':
    app.run(debug=True)
