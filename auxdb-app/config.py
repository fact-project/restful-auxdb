import os
import yaml


config = {}

config_files = (
    os.path.join(os.environ['HOME'], '.restful-auxdb', 'config.yaml'),
    'config.yaml',
)
for config_file in config_files:
    if os.path.isfile(config_file):
        with open(config_file) as f:
            config.update(yaml.safe_load(f))

if 'FACT_AUX_MONGODB_USER' in os.environ:
    config['mongodb']['user'] = os.environ['FACT_AUX_MONGODB_USER']

if 'FACT_AUX_MONGODB_HOST' in os.environ:
    config['mongodb']['host'] = os.environ['FACT_AUX_MONGODB_HOST']

if 'FACT_AUX_MONGODB_PORT' in os.environ:
    config['mongodb']['port'] = os.environ['FACT_AUX_MONGODB_PORT']

if 'FACT_AUX_MONGODB_PASSWORD' in os.environ:
    config['mongodb']['password'] = os.environ['FACT_AUX_MONGODB_PASSWORD']
