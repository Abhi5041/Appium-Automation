import os
from pathlib import Path
import configparser
path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "config.ini")
def readConfig(section,key):
        config = configparser.ConfigParser()
        config.read(config_path)

        return config.get(section,key)

