from flask_restful import Resource, reqparse, marshal_with, fields
from flask.json import jsonify
from .database import database
from datetime import datetime

collection = database.magic_weather

parser = reqparse.RequestParser()
parser.add_argument('field', action='append')
parser.add_argument('from', type=datetime)
parser.add_argument('until', type=datetime)


resource_fields = {
    'timestamp': fields.DateTime(dt_format='iso8601')
}


class MagicWeatherResource(Resource):
    def get(self):
        args = parser.parse_args(strict=True)
        print(args['field'])

        query = {}
        projection = {'_id': False}

        if args['field']:
            for field in args['field']:
                projection[field] = True

        if args['from']:
            query['timestamp'] = {'$gt': args['from']}

        if args['until']:
            query['timestamp'] = {'$lt': args['until']}

        return jsonify(list(collection.find(query, projection=projection)))
