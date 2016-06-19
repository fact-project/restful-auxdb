from flask_restful import Resource, reqparse, inputs
from .database import database
from flask_json import as_json

collection = database.magic_weather

parser = reqparse.RequestParser()
parser.add_argument('field', action='append')
parser.add_argument('from', type=inputs.datetime_from_iso8601)
parser.add_argument('until', type=inputs.datetime_from_iso8601)


class MagicWeatherResource(Resource):
    @as_json
    def get(self):
        args = parser.parse_args(strict=True)

        query = {}
        projection = {'_id': False}

        if args['field']:
            for field in args['field']:
                projection[field] = True

        if args['from']:
            query['timestamp'] = {'$gt': args['from']}

        if args['until']:
            query['timestamp'] = {'$lt': args['until']}

        return {'objects': collection.find(query, projection=projection)}
