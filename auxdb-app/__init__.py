from flask import Flask
from flask_restful import Api
from .magic_weather import MagicWeatherResource


app = Flask('FACT auxdb rest interface')
api = Api(app)

api.add_resource(MagicWeatherResource, '/magic_weather')
