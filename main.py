from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
import json
import GPIO_controll as gpio

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

class changeRelay(Resource):
    def post(self):
        gpio.changePinOut(1, True)
        return jsonify('success')

api.add_resource(changeRelay, "/relay")

if (__name__ == "__main__"):
    gpio.setUp([])
    app.run(host='0.0.0.0')
    gpio.cleanUp()