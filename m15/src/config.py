import pathlib
import yaml
from os import environ

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'config.yaml'


def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
        if environ.get("PORT", None):
            config["common"].update({"port": environ["PORT"]})
        if environ.get("DATABASE_URL", None):
            config["postgres"].update({"url": environ["DATABASE_URL"]})
    return config


config = get_config(config_path)
