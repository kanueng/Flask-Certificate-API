from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('project')
parser.add_argument('name')
parser.add_argument('frame')

class GenCert(Resource):
    def get(self):
        return {'version': '1.0.0'}

    def put(self):
        return {'hello': 'world'}

api.add_resource(GenCert, '/')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
