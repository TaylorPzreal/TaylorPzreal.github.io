AUTHOR = 'TaylorPzreal'
SITENAME = "TaylorPzreal's Blog"
SITEURL = ""
TIMEZONE = 'CET'
DEFAULT_LANG = 'en'

PATH = "content"
ARTICLE_PATHS = "blogs"
STATIC_PATHS = ['images', 'blogs']
PAGE_PATHS = "pages"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("Github", "https://github.com/TaylorPzreal"),
         ("Knowledge", "https://taylorpzreal.github.io/knowledge/"),
         ("Pelican", "https://getpelican.com/"))

# Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
# )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# COPYRIGHT_YEAR=2025
# TRADEMARK = '你的商标'
# FOOTER_CONTENT = f'© {COPYRIGHT_YEAR} {AUTHOR} | {TRADEMARK} 保留所有权利。'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'pymdownx.superfences': {
            'custom_fences': [{
                'name':
                'mermaid',
                'class':
                'mermaid',
                'format':
                '!!python/name:pymdownx.superfences.fence_div_format'
            }]
        }
    },
    'output_format': 'html5',
}
