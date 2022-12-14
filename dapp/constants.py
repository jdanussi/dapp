"""Docstring"""

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = f"{ROOT_DIR}/resources"
UTILS_DIR = f"{ROOT_DIR}/utils"
CONFIGURATION_FILE = os.path.join(UTILS_DIR, "database.ini")
