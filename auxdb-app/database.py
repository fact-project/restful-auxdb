from pymongo import MongoClient

from .config import config

uri = 'mongodb://{user}:{password}@{host}:{port}'
client = MongoClient(uri.format(**config['mongodb']))
database = client[config['mongodb']['database']]
