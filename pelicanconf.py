# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import os

AUTHOR = u'Kale Franz'
SITENAME = u'NotInKansasNow'
SITEURL = ''

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 6

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

THEME = 'theme'
THEME_STATIC_DIR = 'static'

STATIC_PATHS = ['static', 'CNAME']

DISPLAY_CATEGORIES_ON_MENU = True

MD_EXTENSIONS = ['extra', 'codehilite(css_class=highlight, linenums=False)',
                 'meta']
#PLUGIN_PATH = '../pelican-plugins/'
#PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img']

DISQUS_SITENAME = 'nikn'

TAG_CLOUD_MAX_ITEMS = 7
TAG_CLOUD_STEPS = 4

SUMMARY_END_TEXT = '...'

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# sitemap


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

size_map = {1: 'xs', 2: 'sm', 3: 'md', 4: 'lg'}
def button_size(size):
    return "btn-{}".format(size_map[int(size)])

def strip_index(name):
    idx = name.find("/index")
    if idx > 0:
        return name[0:idx]
    else:
        return name

JINJA_FILTERS = {'format_authors': format_authors,
                 'button_size': button_size,
                 'strip_index': strip_index,
}