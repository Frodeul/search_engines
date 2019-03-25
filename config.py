import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'D8*zmo;n]0UY>ma5UP._;1xKe^|daVxOt^|9eN|tp&uKXZoV#xa8w=>^OA;GwNc'
    TEMPLATES_AUTO_RELOAD = True
