from flask import Flask
from flask_restful import Api
from flask_json import FlaskJSON

from .resources import MagicWeatherResource

app = Flask('FACT auxdb rest interface')
api = Api(app)
json = FlaskJSON(app)

api.add_resource(MagicWeatherResource, '/magic_weather')
