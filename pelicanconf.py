#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Michael Adcock'
SITENAME = 'Michael Adcock'
SITEURL = 'https://michael-adcock.github.io/'
SITESUBTITLE = 'Data Scientist'
#SITEDESCRIPTION = 'Projects related to data science'


PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#EXTRA_PATH_METADATA = {
#    'extra/custom.css': {'path': 'static/custom.css'},
#}
#CUSTOM_CSS = 'static/custom.css'
#BROWSER_COLOR = '#333333'
#PYGMENTS_STYLE = 'monokai'

# Blogroll

SOCIAL = (('github', 'https://github.com/michael-adcock'),
         ('linkedin', 'https://www.linkedin.com/in/m-t-adcock/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
#, 'rmd_reader']

THEME = "pelican-themes/Flex"

STATIC_PATHS = ['figures']
RMD_READER_RENAME_PLOT = 'directory'
RMD_READER_KNITR_OPTS_CHUNK = {'fig.path': 'figures/'}
