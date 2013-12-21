# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'Kale Franz'
SITENAME = u'NotInKansasNow'
SITEURL = ''

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 120

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Formatting for dates

DEFAULT_DATE_FORMAT = ('%b %d, %Y')

# Formatting for urls

ARTICLE_URL = "{category}/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{category}/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "{slug}/"
CATEGORY_SAVE_AS = "{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

AUTHOR_URL = "{slug}/"
AUTHOR_SAVE_AS = "{slug}/index.html"

DIRECT_TEMPLATES = ('index', 'tags', 'archives')

ARTICLE_DIR = 'articles'

THEME = 'theme'
THEME_STATIC_DIR = 'static'

STATIC_PATHS = ['static', 'CNAME', 'robots.txt', 'google3df5b54978a512de.html']
#EXTRA_PATH_METADATA = {
#    'extra': {'path': '../'},
#    }

DISPLAY_CATEGORIES_ON_MENU = True

MD_EXTENSIONS = ['extra', 'codehilite(css_class=highlight, linenums=False)',
                 'meta']

DISQUS_SITENAME = 'nikn'

TAG_CLOUD_MAX_ITEMS = 9
TAG_CLOUD_STEPS = 4

SUMMARY_END_TEXT = '...'

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

PLUGIN_PATH = 'plugins/'
PLUGINS = ['sitemap',]

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