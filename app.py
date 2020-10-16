from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class lmao(Resource):
    def get(self):
        return {"data": "Started Python, LOL!"}

api.add_resource(lmao, "/")

if __name__ == "__main__":
    app.run(debug=True)