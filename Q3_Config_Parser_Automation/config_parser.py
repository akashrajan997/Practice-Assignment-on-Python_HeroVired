import configparser
import json
import sys

INI_FILE = "sample_config.ini"
JSON_FILE = "config_output.json"

def parse_config(ini_path):
    config = configparser.ConfigParser()
    config.read(ini_path)
    result = {}
    for section in config.sections():
        for key, value in config.items(section):
            result[f"{section}.{key}"] = value
    return result

def save_as_json(data, json_path):
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    try:
        data = parse_config(INI_FILE)
        save_as_json(data, JSON_FILE)
        print(f"Config parsed and saved to {JSON_FILE}")
    except Exception as e:
        print(f"Error: {e}")
