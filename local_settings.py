#local_settings.py
# -*- coding: utf-8 -*-

AUTHOR = 'Name'
SITENAME = 'opg'
SITEURL = 'http://site.org'

TIMEZONE = 'Europe/Moscow'

LOCALE = 'ru_RU.UTF-8'
DEFAULT_LANG = 'ru'

# Plugins
PLUGIN_PATH = "plugins"
PLUGINS = ["sitemap", ]
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

# путь к исходникам
PATH = 'content'
# путь к выходным html-файлам
# в целом настройка не важна,
# ибо генерировать всё, кроме постов
# будем в корень проекта
OUTPUT_PATH = 'articles/'
# как сохранять посты
ARTICLE_URL = 'articles/{slug}/'
# куда сохранять посты
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'