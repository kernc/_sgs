#!/usr/bin/env python

## Development ######################################################

RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

CACHE_CONTENT = False
LOAD_CONTENT_CACHE = True
GZIP_CACHE = False

SITEURL = 'https://godalni-sekstet.si'
# ~ SITEURL = 'http://localhost:8000'

assert not SITEURL.endswith('/')

## Pelican settings #################################################

AUTHOR = 'Slovenski godalni sekstet'
SITENAME = 'Slovenski godalni sekstet'

PATH = 'content'
OUTPUT_PATH = 'output/'
READERS = {
    'rst': None,  # Disable docutils/reST
}

TIMEZONE = 'Europe/Ljubljana'
DATE_FORMATS = {
    'en': ('en_IE.utf8', '%-d %b %Y'),
    'sl': ('sl_SI.utf8', '%-d. %B %Y'),
}
LOCALE = (
    # On Windos
    'sl', 'en',
    # On Unix/Linux
    'sl_SI.utf8', 'en_IE.utf8',
)

DEFAULT_LANG = 'sl'
ARTICLE_TRANSLATION_ID = 'translation_id'
PAGE_TRANSLATION_ID = 'translation_id'

DEFAULT_METADATA = {
    'lang': 'sl',
    'page_order': '9'
}
FILENAME_METADATA = '((?P<date>\d{4}-\d{2}-\d{2})-)?(?P<translation_id>.*)'
PATH_METADATA = '(pages|objave)/(?P<lang>en)/.*'

THEME = 'theme'
THEME_STATIC_DIR = 'static'

PAGE_ORDER_BY = 'page_order'

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feed.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

DIRECT_TEMPLATES = ['index']

ARTICLE_URL = '{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_LANG_URL = '{lang}/' + ARTICLE_URL
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL + 'index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_LANG_URL = '{lang}/' + PAGE_URL
PAGE_LANG_SAVE_AS = PAGE_LANG_URL + 'index.html'

STATIC_LANG_URL = '{path}'  # == STATIC_URL
STATIC_LANG_SAVE_AS = '{path}'  # == STATIC_SAVE_AS

AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''

SLUG_REGEX_SUBSTITUTIONS = [
   ('č', 'c'),
   ('ž', 'z'),
   ('š', 's'),
   (r'\A\s*', ''), # strip leading whitespace
   (r'\s*\Z', ''), # strip trailing whitespace
   (r'\W+', '-'),  # reduce non-alphanumerics to single '-'
]

TYPOGRIFY = True

MARKDOWN = dict(
    output_format='html5',
    extensions=[
        'markdown.extensions.meta',
        'markdown.extensions.toc',  # For header-id
        'markdown.extensions.md_in_html',  # For contact <address>
        'markdown.extensions.attr_list',
        'markdown.extensions.footnotes',
    ],
    extension_configs={
        "markdown.extensions.smarty": dict(
            smart_dashes=True,
            smart_ellipses=True,
            smart_quotes=False,
            smart_angled_quotes=False,
        ),
    },
)

STATIC_PATHS = [
    'images',
    'static',
]
EXTRA_PATH_METADATA = {
    'static': {'path': ''},
}

## Plugins ###########################################################

PLUGIN_PATHS = ['my-plugins', 'pelican-plugins']
PLUGINS = []
PLUGINS.append('css-html-js-minify')
PLUGINS.append('optimize_images')
PLUGINS.append('w3c_validate')

PLUGINS.append('sitemap')
SITEMAP = {
    'format': 'txt',
    'exclude': [],
}

# ~ PLUGINS.append('deadlinks')
DEADLINK_VALIDATION = True
DEADLINK_OPTS = {
    'timeout_duration_ms': 10000,
    'timeout_is_error': True,
}

def T(label, lang, _TRANS={
        'en': {
            SITENAME: 'Slovenian String Sextet',
            '<span>Slovenski</span><br>godalni sekstet': '<span>Slovenian</span><br>String Sextet',
            'Zadnje objave': 'Latest news',
        }}):
    try:
        return _TRANS[lang][label]
    except KeyError:
        return label


PLUGINS.append('image_process')
IMAGE_PROCESS_DIR = ''
IMAGE_PROCESS = {
    'homepage': {
        'type': 'responsive-image',
        'default': '1920w',
        'sizes': '100vw',
        'srcset': [
            ('400w', ['scale_out 400 0 False']),
            ('600w', ['scale_out 600 0 False']),
            ('800w', ['scale_out 800 0 False']),
            ('1024w', ['scale_out 1024 0 False']),
            ('1366w', ['scale_out 1366 0 False']),
            ('1600w', ['scale_out 1600 0 False']),
            ('1920w', ['scale_out 1920 0 False']),
        ],
    },
    'parallax': {
        'type': 'responsive-image',
        'default': '1920w',
        'sizes': '100vw',
        'srcset': [
            ('400w', ['scale_out 400 0 False']),
            ('600w', ['scale_out 600 0 False']),
            ('800w', ['scale_out 800 0 False']),
            ('1024w', ['scale_out 1024 0 False']),
            ('1366w', ['scale_out 1366 0 False']),
            ('1600w', ['scale_out 1600 0 False']),
            ('1920w', ['scale_out 1920 0 False']),
        ],
    },
    'gallery': {
        'type': 'responsive-image',
        'default': '1200w',
        'sizes': '(min-width: 1200px) 31vw, '
                 '(min-width: 800px) 46vw, '
                 '95vw',
        'srcset': [
            ('400w', ['scale_out 400 0 False']),
            ('600w', ['scale_out 600 0 False']),
            ('800w', ['scale_out 800 0 False']),
            ('1000w', ['scale_out 1000 0 False']),
            ('1200w', ['scale_out 1200 0 False']),
        ],
    },
    'sextet-members': {
        'type': 'responsive-image',
        'default': '1000w',
        'sizes': '(min-width: 1100px) 1000px,'
                 '100vw',
        'srcset': [
            ('400w', ['scale_out 400 0 False']),
            ('600w', ['scale_out 600 0 False']),
            ('800w', ['scale_out 800 0 False']),
            ('1000w', ['scale_out 1000 0 False']),
        ],
    },
    'mugshot': {
        'type': 'responsive-image',
        'default': '400w',
        'sizes': '(min-width: 600px) 400px, '
                 '100vw',
        'srcset': [
            ('300w', ['scale_in 300 300 False']),
            ('400w', ['scale_in 400 400 False']),
        ],
    },
    'article': {
        'type': 'responsive-image',
        'default': '1920w',
        'sizes': '100vw',
        'srcset': [
            ('400w', ['scale_out 400 0 False']),
            ('600w', ['scale_out 600 0 False']),
            ('800w', ['scale_out 800 0 False']),
            ('1024w', ['scale_out 1024 0 False']),
            ('1366w', ['scale_out 1366 0 False']),
            ('1600w', ['scale_out 1600 0 False']),
            ('1920w', ['scale_out 1920 0 False']),
        ],
    },
}


## Custom template values ###########################################

from datetime import datetime
CURRENT_YEAR = datetime.now().year

MENU_LANG = {
    'en': '🇬🇧 EN',
    'sl': '🇸🇮 SL',
}

LOGO_LINKS = [
    ('Glasbena mladina ljubljanska', 'https://www.gml-drustvo.si'),
    ('Nauportus Viva', 'https://nauportus.wordpress.com'),
    ('Revija Glasna', 'http://www.revijaglasna.si'),
    ('Mestni muzej Ljubljana', 'https://mgml.si/sl/mestni-muzej/'),
    ('Hiša kulture Celje', 'http://www.hisakulture.si'),
    ('Kulturno društvo Kropa', 'https://kultura-kropa.si'),
    ('ZRC SAZU', 'https://www.zrc-sazu.si'),
    ('Radio televizija Slovenija', 'https://www.rtvslo.si/rtv/kdo-smo/glasbena-produkcija'),
    ('Imago Sloveniae', 'https://imagosloveniae.net'),
    ('Univerza v Ljubljani, Akademija za glasbo', 'http://www.ag.uni-lj.si'),
    ('Republika Slovenija, Ministrstvo za kulturo', 'http://mk.gov.si'),
    ('I Feel Slovenia', 'https://www.slovenia.info'),
]

def TOP_ARTICLES(articles, lang):
    if lang == DEFAULT_LANG:
        return articles
    return [translation
            for article in articles
            for translation in article.translations
            if translation.lang == lang]
