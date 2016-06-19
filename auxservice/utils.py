import dateutil.parser


def convert_to_datetime(string):
    return dateutil.parser.parse(string)


def build_from_until_query(from_=None, until=None, key='timestamp'):

        if not from_ and not until:
            return {}
        elif from_ and not until:
            return {'timestamp': {'$gt': from_}}

        elif not from_ and until:
            return {'timestamp': {'$lt': until}}

        elif from_ and until:
            return {'$and': [
                 {'timestamp': {'$lt': until}},
                 {'timestamp': {'$gt': from_}},
            ]}
