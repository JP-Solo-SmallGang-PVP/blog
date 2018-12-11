#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Japanese PvPers'
SITENAME = 'JP Solo/Small Gang PVP'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%d, %-m %Y'
THEME = 'theme'

FAVICON = 'favicon.jpg'
FAVICON_TYPE = 'image/jpg'

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/' + FAVICON: { 'path': FAVICON },
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = 'feeds/all-{lang}.atom.xml'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
MENUITEMS = (('About', 'about.html'),
             ('Join(Discord)', 'https://discord.gg/FcYrc47'),
             ('Archives', 'archives.html'),
             ('Feed', 'feeds/all-en.atom.xml'),)

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True