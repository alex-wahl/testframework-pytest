import os
from enum import Enum

WORKING_DIRECTORY = os.getcwd()
WEBDRIVER = f"{WORKING_DIRECTORY}/resources/webdrivers"


class Environment(Enum):
    PROD = 'https://ikea.de'
    QA = 'https://qa.ikea.com'
