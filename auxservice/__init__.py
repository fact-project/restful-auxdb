from flask import Flask, render_template
from flask_restful import Api
from flask_json import FlaskJSON
from .database import database

from .resources import (
    MagicWeatherResource,
    PfMiniResource,
    DriveSourceResource,
    DrivePointingResource,
    DriveTrackingResource,
)

app = Flask(__name__)
api = Api(app)
json = FlaskJSON(app)

api.add_resource(MagicWeatherResource, '/magic_weather')
api.add_resource(PfMiniResource, '/pf_mini')
api.add_resource(DriveTrackingResource, '/drive_tracking')
api.add_resource(DrivePointingResource, '/drive_pointing')
api.add_resource(DriveSourceResource, '/drive_source')


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/services')
def services():
    services = database.collection_names()
    services.remove('system.indexes')
    services.sort()
    return render_template('services.html', services=services)


@app.route('/services/<service>')
def service(service):
    entry = database[service].find_one()
    fields = list(entry.keys())
    fields.remove('_id')
    fields.sort()
    return render_template('service.html', fields=fields, service=service)
