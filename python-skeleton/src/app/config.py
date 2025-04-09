from os import getenv

from distutils.util import strtobool

ENV = getenv('ENV', 'local')
DEBUG = bool(strtobool(getenv('DEBUG', 'False')))
