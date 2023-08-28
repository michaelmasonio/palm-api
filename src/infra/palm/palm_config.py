import json


def load_config():
    # Read the configuration from config.json
    with open("secrets.json") as f:
        config = json.load(f)

    return config
