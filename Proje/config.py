import os
class Config(object):
    os.environ.get('SECRET_KEY') or 'never-guess'

    