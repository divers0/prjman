import json

from .const import CONFIG_FILE_PATH


def read_config_file():
    with open(CONFIG_FILE_PATH, "r") as f:
        config_file = json.load(f)
    return config_file


def write_to_config_file(new_config):
    with open(CONFIG_FILE_PATH, "w") as f:
        json.dump(new_config, f)


def get_paths():
    return read_config_file()["paths"]


def add_to_paths(new_paths):
    config_file = read_config_file()
    config_file["paths"] += new_paths
    write_to_config_file(config_file)
