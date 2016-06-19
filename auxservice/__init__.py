from flask import Flask
from flask_restful import Api
from flask_json import FlaskJSON

from .resources import (
    MagicWeatherResource,
    PfMiniResource,
    DriveSourceResource,
    DrivePointingResource,
    DriveTrackingResource,
)

app = Flask('FACT auxdb rest interface')
api = Api(app)
json = FlaskJSON(app)

api.add_resource(MagicWeatherResource, '/magic_weather')
api.add_resource(PfMiniResource, '/pf_mini')
api.add_resource(DriveTrackingResource, '/drive_tracking')
api.add_resource(DrivePointingResource, '/drive_pointing')
api.add_resource(DriveSourceResource, '/drive_source')
