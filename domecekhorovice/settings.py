"""
Django settings for domecekhorovice project.
"""

from django.utils.translation import ugettext_lazy as _
from leprikon.site.settings import *

# Application definition
INSTALLED_APPS = (
    [
        "domecekhorovice",
    ]
    + INSTALLED_APPS
    + [
        "cms_articles",
        # "djangocms_icon",
        # "djangocms_link",
        # "djangocms_picture",
        # "djangocms_bootstrap5",
        # "djangocms_bootstrap5.contrib.bootstrap5_alerts",
        # "djangocms_bootstrap5.contrib.bootstrap5_badge",
        # "djangocms_bootstrap5.contrib.bootstrap5_card",
        # "djangocms_bootstrap5.contrib.bootstrap5_carousel",
        # "djangocms_bootstrap5.contrib.bootstrap5_collapse",
        # "djangocms_bootstrap5.contrib.bootstrap5_content",
        # "djangocms_bootstrap5.contrib.bootstrap5_grid",
        # "djangocms_bootstrap5.contrib.bootstrap5_jumbotron",
        # "djangocms_bootstrap5.contrib.bootstrap5_link",
        # "djangocms_bootstrap5.contrib.bootstrap5_listgroup",
        # "djangocms_bootstrap5.contrib.bootstrap5_media",
        # "djangocms_bootstrap5.contrib.bootstrap5_picture",
        # "djangocms_bootstrap5.contrib.bootstrap5_tabs",
        # "djangocms_bootstrap5.contrib.bootstrap5_utilities",
    ]
)

CMS_TEMPLATES = [
    ("default.html", "Výchozí"),
]

# templates used to render plugin article
# CMS_ARTICLES_PLUGIN_ARTICLE_TEMPLATES = [
#     ("default", "Výchozí"),
# ]

# templates used to render plugin articles
# CMS_ARTICLES_PLUGIN_ARTICLES_TEMPLATES = [
#     ("default", "Výchozí"),
#     ("menu", "Menu"),
# ]

CMS_PLACEHOLDER_CONF = {
    "content": {
        "name": "Obsah",
    },
}

THUMBNAIL_ALIASES = {
    "": {
        "preview": {
            "size": (240, 10000),
        },
        "view": {
            "size": (760, 570),
        },
    },
}

# search settings
# HAYSTACK_CONNECTIONS = {
#     "default": {
#         "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
#         "PATH": os.path.join(BASE_DIR, "data", "search"),
#     },
#     "cs": {
#         "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
#         "PATH": os.path.join(BASE_DIR, "data", "search"),
#     },
# }
