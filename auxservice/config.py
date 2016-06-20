import os
import yaml
from collections import Mapping


def update(d, u):
    '''
    Update a dict recursively
    from http://stackoverflow.com/a/3233356/3838691
    '''
    for k, v in u.items():
        if isinstance(v, Mapping):
            r = update(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]
    return d

config = {
    'mongodb': {
        'host': 'mongo',
        'database': 'auxdata',
        'port': 27017,
    },
    'users': {},
}

config_files = (
    os.path.join(os.environ['HOME'], '.restful-auxdb', 'config.yaml'),
    'config.yaml',
)
for config_file in config_files:
    if os.path.isfile(config_file):
        with open(config_file) as f:
            config = update(config, yaml.safe_load(f))

if 'FACT_AUX_MONGODB_USER' in os.environ:
    config['mongodb']['user'] = os.environ['FACT_AUX_MONGODB_USER']

if 'FACT_AUX_MONGODB_HOST' in os.environ:
    config['mongodb']['host'] = os.environ['FACT_AUX_MONGODB_HOST']

if 'FACT_AUX_MONGODB_PORT' in os.environ:
    config['mongodb']['port'] = os.environ['FACT_AUX_MONGODB_PORT']

if 'FACT_AUX_MONGODB_PASSWORD' in os.environ:
    config['mongodb']['password'] = os.environ['FACT_AUX_MONGODB_PASSWORD']

if 'FACT_AUX_MONGODB_DATABASE' in os.environ:
    config['mongodb']['database'] = os.environ['FACT_AUX_MONGODB_DATABASE']

if 'FACT_AUX_USER' in os.environ and 'FACT_AUX_PASSWORD' in os.environ:
    config['users'].update(
        {os.environ['FACT_AUX_USER']: os.environ['FACT_AUX_PASSWORD']}
    )
