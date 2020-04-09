# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)
api = Api(app)

# Require a parser to parse our POST request.
parser = reqparse.RequestParser()
parser.add_argument("arg01")


class MyApi(Resource):
    def post(self):
        args = parser.parse_args()
        val = args['arg01']
        val_val = val + ' ---> flask heroku'

        # === save data as pickle ===
        # path = 'myData.pkl'
        # with open(path, mode='wb') as f:
        #     pickle.dump(val_val, f)

        return {"after_api": val_val}


api.add_resource(MyApi, "/myapi")

if __name__ == "__main__":
    app.run('127.0.0.1', 5002, debug=False)
