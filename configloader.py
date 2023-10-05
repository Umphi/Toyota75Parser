import configparser
import os


def load_config(filename):
    if not os.path.exists(f"./settings.ini"):
        print("Config file (settings.ini) is not provided. Please, use \"settings.ini.example\" to create config.")
        exit(1)
    config = configparser.ConfigParser()
    config.read(filename)
    return config
