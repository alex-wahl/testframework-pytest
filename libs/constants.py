import os
from enum import Enum

WORKING_DIRECTORY = os.getcwd()


class Environment(Enum):
    PROD = 'https://ikea.de'
    QA = 'https://qa.ikea.com'
