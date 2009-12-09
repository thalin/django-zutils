#!/usr/bin/env python
'''
Created Dec. 9, 2009

@author: thalin

Setup script for django-zutils
'''
from distutils.core import setup

setup_dict = {
    'name': 'zutils',
    'version': '.1a',
    'description': "Zeke's utilities for Django",
    'author': 'Zeke Harris (thalin)',
    'author_email': 'thalin@zen-finity.com',
    'url': 'http://github.com/thalin/django-zutils',
    'packages': ['zutils']
}

setup(**setup_dict)
