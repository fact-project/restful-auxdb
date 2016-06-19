from flask_httpauth import HTTPBasicAuth
from .config import config

auth = HTTPBasicAuth()


@auth.get_password
def get_pw(username):
    return config['users'].get(username, None)
