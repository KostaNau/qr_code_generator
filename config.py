# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


DEBUG = True
SECRET_KEY = 'This key must be secret!'
WTF_CSRF_ENABLED = True

try:
    from config_local import *
except ImportError:
    pass

