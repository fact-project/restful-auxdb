from flask_restful import Resource, reqparse
from .database import database as db
from flask_json import as_json
from .utils import convert_to_datetime
from .utils import build_from_until_query
from .auth import auth
from pymongo.errors import ConnectionFailure

parser = reqparse.RequestParser()
parser.add_argument('field', action='append')
parser.add_argument('from', type=convert_to_datetime)
parser.add_argument('until', type=convert_to_datetime)


class AuxResource(Resource):
    method_decorators = [auth.login_required]
    collection = None

    @as_json
    def get(self):
        args = parser.parse_args(strict=True)

        projection = {'_id': False}

        if args['field']:
            for field in args['field']:
                projection[field] = True

        query = build_from_until_query(args['from'], args['until'])

        try:
            return {
                self.collection.name: self.collection.find(
                    query, projection=projection
                ),
                'success': True,
            }
        except ConnectionFailure:
            return {'success:', False}, 503


class MagicWeatherResource(AuxResource):
    collection = db.magic_weather


class PfMiniResource(AuxResource):
    collection = db.pf_mini


class DriveTrackingResource(AuxResource):
    collection = db.drive_tracking


class DrivePointingResource(AuxResource):
    collection = db.drive_pointing


class DriveSourceResource(AuxResource):
    collection = db.drive_source


class FSCHumidityResource(AuxResource):
    collection = db.fsc_humidity


class FSCTemperatureResource(AuxResource):
    collection = db.fsc_temperature


class FTMTriggerRatesResource(AuxResource):
    collection = db.ftm_trigger_rates
