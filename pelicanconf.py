#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Timothy Pulliam'
SITENAME = 'linuxandchill'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'extra',]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
DEFAULT_METADATA = {
        'status': 'draft',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# https://python-markdown.github.io/extensions/code_hilite/
MARKDOWN = {'extension_configs': {'markdown.extensions.codehilite': {'css_class': 'highlight', 'use_pygments': True, 'guess_lang': False,},
                                    'markdown.extensions.extra': {},
                                    'markdown.extensions.meta': {}},
                                    'output_format': 'html5'}
