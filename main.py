from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
import json
import GPIO_controll as gpio

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

class changeRelayHigh(Resource):
    def get(self):
        gpio.changePinOut(14, True)
        return jsonify('success')

class changeRelayLow(Resource):
    def get(self):
        gpio.changePinOut(14, False)
        return jsonify('success')

api.add_resource(changeRelayHigh, "/relayHigh")
api.add_resource(changeRelayLow, "/relayLow")


if (__name__ == "__main__"):
    gpio.setUp([14])
    app.run(host='0.0.0.0')
    gpio.cleanUp()