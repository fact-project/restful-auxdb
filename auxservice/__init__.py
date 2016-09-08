from flask import Flask, render_template
from flask_restful import Api
from flask_json import FlaskJSON
from .database import database
from pymongo.errors import ConnectionFailure

from .resources import (
    MagicWeatherResource,
    PfMiniResource,
    DriveSourceResource,
    DrivePointingResource,
    DriveTrackingResource,
    FSCHumidityResource,
    FSCTemperatureResource,
    FTMTriggerRatesResource,
)

app = Flask(__name__)
api = Api(app)
json = FlaskJSON(app)

api.add_resource(MagicWeatherResource, '/magic_weather')
api.add_resource(PfMiniResource, '/pf_mini')
api.add_resource(DriveTrackingResource, '/drive_tracking')
api.add_resource(DrivePointingResource, '/drive_pointing')
api.add_resource(DriveSourceResource, '/drive_source')
api.add_resource(FSCHumidityResource, '/fsc_humidity')
api.add_resource(FSCTemperatureResource, '/fsc_temperature')
api.add_resource(FTMTriggerRatesResource, '/ftm_trigger_rates')

ignored_collections = ('system.indexes', 'str', 'type')


def get_services():
    services = database.collection_names()
    services = list(filter(lambda s: s not in ignored_collections, services))
    services.sort()

    return services


@app.route('/')
def main_page():
    return render_template('index.html', services=get_services())


@app.route('/services')
def service_overview():
    return render_template('services.html', services=get_services())


@app.route('/services/<service>')
def service(service):
    try:
        entry = database[service].find_one()
    except ConnectionFailure:
        entry = {}
    fields = list(entry.keys())
    if fields:
        fields.remove('_id', )
        fields.sort()

    return render_template(
        'service.html', fields=fields, service=service, services=get_services()
    )
