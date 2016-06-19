from flask_restful import Resource, reqparse
from .database import database
from flask_json import as_json
from .utils import convert_to_datetime
from .utils import build_from_until_query


collection = database.magic_weather

parser = reqparse.RequestParser()
parser.add_argument('field', action='append')
parser.add_argument('from', type=convert_to_datetime)
parser.add_argument('until', type=convert_to_datetime)


class MagicWeatherResource(Resource):
    @as_json
    def get(self):
        args = parser.parse_args(strict=True)

        query = {}
        projection = {'_id': False}

        if args['field']:
            for field in args['field']:
                projection[field] = True

        query = build_from_until_query(args['from'], args['until'])

        return {'objects': collection.find(query, projection=projection)}
