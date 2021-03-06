from django.conf import settings
import os

LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'
USE_L10N = True
USE_TZ = True
USE_I18N = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGUAGES = (
('en', u'English'),
('pt-br', u'Português'),
('es', u'Español')
)
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)


# Global martor settings
# Input: string boolean, `true/false`
MARTOR_ENABLE_CONFIGS = getattr(
    settings, 'MARTOR_ENABLE_CONFIGS', {
        'imgur': 'true',      # to enable/disable imgur/custom uploader.
        'mention': 'false',   # to enable/disable mention
        'jquery': 'true',     # to include/revoke jquery (require for admin default django)
        'living': 'false',    # to enable/disable live updates in preview
    }
)

# To setup the martor editor with label or not (default is False)
MARTOR_ENABLE_LABEL = getattr(
    settings, 'MARTOR_ENABLE_LABEL', False
)

# Imgur API Keys
MARTOR_IMGUR_CLIENT_ID = getattr(
    settings, 'MARTOR_IMGUR_CLIENT_ID', ''
)
MARTOR_IMGUR_API_KEY = getattr(
    settings, 'MARTOR_IMGUR_API_KEY', ''
)

# Safe Mode
MARTOR_MARKDOWN_SAFE_MODE = getattr(
    settings, 'MARTOR_MARKDOWN_SAFE_MODE', True
)

# Markdownify
MARTOR_MARKDOWNIFY_FUNCTION = getattr(
    settings, 'MARTOR_MARKDOWNIFY_FUNCTION', 'martor.utils.markdownify'
)
MARTOR_MARKDOWNIFY_URL = getattr(
    settings, 'MARTOR_MARKDOWNIFY_URL', '/martor/markdownify/'
)

# Markdown extensions
MARTOR_MARKDOWN_EXTENSIONS = getattr(
    settings, 'MARTOR_MARKDOWN_EXTENSIONS', [
        'markdown.extensions.extra',
        'markdown.extensions.nl2br',
        'markdown.extensions.smarty',
        'markdown.extensions.fenced_code',

        # Custom markdown extensions.
        'martor.extensions.urlize',
        'martor.extensions.del_ins',    # ~~strikethrough~~ and ++underscores++
        'martor.extensions.mention',    # to parse markdown mention
        'martor.extensions.emoji',      # to parse markdown emoji
        'martor.extensions.mdx_video',  # to parse embed/iframe video
    ]
)

# Markdown Extensions Configs
MARTOR_MARKDOWN_EXTENSION_CONFIGS = getattr(
    settings, 'MARTOR_MARKDOWN_EXTENSION_CONFIGS', {}
)

# Markdown urls
MARTOR_UPLOAD_URL = getattr(
    settings, 'MARTOR_UPLOAD_URL', '/martor/uploader/'  # for imgur
)
MARTOR_SEARCH_USERS_URL = getattr(
    settings, 'MARTOR_SEARCH_USERS_URL', '/martor/search-user/'  # for mention
)

# Markdown Extensions
MARTOR_MARKDOWN_BASE_EMOJI_URL = getattr(
    settings, 'MARTOR_MARKDOWN_BASE_EMOJI_URL', 'https://assets-cdn.github.com/images/icons/emoji/'
)
MARTOR_MARKDOWN_BASE_MENTION_URL = getattr(
    settings, 'MARTOR_MARKDOWN_BASE_MENTION_URL', 'https://python.web.id/author/'
)
