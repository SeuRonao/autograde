"""
Configuration module.
"""

import configparser
from pathlib import Path

config = configparser.ConfigParser()

config_filepath = (Path(__file__).parent.parent / 'config.ini').resolve()

config.read(config_filepath.as_posix())
