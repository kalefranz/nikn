# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import collections
from datetime import datetime
import jinja2
import re

AUTHOR = u'Kale Franz'
AUTHOR_FULL = u'Kale J. Franz, PhD'
SITENAME = u'NotInKansasNow'
SITEURL = ''

TIMEZONE = 'US/Pacific'


## Paths ##
###########

PATH = 'content/'  # Path to content directory to be processed
OUTPUT_PATH = 'output/'
PAGE_DIR = 'pages/'
ARTICLE_DIR = 'articles/'

STATIC_PATHS = ['static', 'CNAME', 'robots.txt', 'google3df5b54978a512de.html']

THEME = 'theme/'
THEME_STATIC_DIR = 'static/'

DIRECT_TEMPLATES = ('index', 'tags', 'archives')

TEMPLATE_PAGES = {'404.html': '404.html'}


## URL SETTINGS ##
##################
ARTICLE_URL = "{category}/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{category}/{date:%Y}/{date:%m}/{slug}/index.html"
CATEGORY_URL = "{slug}/"
CATEGORY_SAVE_AS = "{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = "{slug}/"
AUTHOR_SAVE_AS = "{slug}/index.html"


## OTHER ##
###########
DEFAULT_DATE_FORMAT = ('%b %d, %Y')
USE_FOLDER_AS_CATEGORY = True

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 50

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

TAG_CLOUD_MAX_ITEMS = 9
TAG_CLOUD_STEPS = 4

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)


## PLUGIN SETTINGS ##
#####################
PLUGIN_PATH = 'plugins/'
PLUGINS = ['sitemap',]

#sudo wget -P /usr/local/lib/python2.7/site-packages/markdown/extensions/ https://raw.github.com/sgraber/markdown.superscript/master/superscript.py
#sudo wget -P /usr/local/lib/python2.7/site-packages/markdown/extensions/ https://raw.github.com/sgraber/markdown.subscript/master/subscript.py
MD_EXTENSIONS = ['extra',
                 'codehilite(css_class=highlight, linenums=False)',
                 'meta']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


## PERSONAL PELICAN BUILD SETTINGS ##
#####################################
SUMMARY_END_TEXT = '...'


## EXTRA SETTINGS ##
####################

GOOGLE_ANALYTICS_ID = ''
GOOGLE_ANALYTICS_SITE = ''

DISQUS_SITENAME = 'nikn'


## JINJA ##
###########

def format_authors(authors_str):
    authors = [a.strip() for a in authors_str.replace(' and ', ',').split(',')]
    authors = filter(bool, authors)
    l = len(authors)
    if l == 1:
        return authors[0]
    elif l == 2:
        return " and ".join(authors)
    elif l > 2:
        return ", ".join(authors)

def strip_index(name):
    name = name.rstrip('/')
    name = name.rstrip('index')
    name = name.rstrip('/')
    if name and name[0] != '/':
        name = '/' + name
    return name

JINJA_FILTERS = {'format_authors': format_authors,
                 'strip_index': strip_index,
                }

@jinja2.contextfunction
def get_context(c):
    return collections.OrderedDict(sorted(c.items(), key=lambda t: t[0]))

JINJA_GLOBALS = {'context': get_context,
                 'callable': callable,
                 'dirvar': dir,
                 'now': datetime.now
                }


def _is_re_match(s, rs):
    """Allows testing based on a regex"""
    # https://groups.google.com/forum/#!topic/pocoo-libs/3yZl8vHJ9fI
    return True if re.search(rs, s) else False

JINJA_TESTS = {'re_match': _is_re_match}