from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Saludar(Resource):
    def get(self):
        return {'message': 'Buenos días.'}


api.add_resource(Saludar, '/')

if __name__ == '__main__':
    app.run(debug=True)
