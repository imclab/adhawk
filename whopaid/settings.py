# Django settings for whopaid project.
from local_settings import *
from logging.handlers import SMTPHandler
import os.path

SITE_ROOT = os.path.realpath(
        os.path.join(os.path.dirname(__file__),
            os.path.pardir))

POSTMARK_API_KEY = '***REMOVED***'

AWS_ACCESS_KEY_ID = '***REMOVED***'
AWS_SECRET_ACCESS_KEY = '***REMOVED***'
AWS_STORAGE_BUCKET_NAME = 'assets.adhawk'
AWS_IS_GZIPPED = False
AWS_S3_SECURE_URLS = False

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('timbal', 'timball@sunlightfoundation.com'),
    ('bob pants', 'blannon@sunlightfoundation.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = os.path.join(SITE_ROOT,'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, 'site_static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whopaid.storage.CachedS3BotoStorage'

ADMIIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'y=r5im3zl3*7g-f-6dx6^58y@4)%ufsup!w^96uayyp#16q$yw'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)



MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'whopaid.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'whopaid.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT,'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'spammer',
    'search',
    'haystack',
    'knowledge_base',
    'whopaid',
    'whopaid_api',
    'fts',
    'db_script',
    'south',

    'debug_toolbar',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    #'filters': {
    #    'require_debug_false': {
    #        '()': 'django.utils.log.RequireDebugFalse'
    #    }
    #},
    'handlers': {
        'matching' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'echoprint_server_api/match_report.log'),
        },
        'fp_querying' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'echoprint_server_api/fp.log'),
        },
        'ad_media_importing' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/ad_media_importer.log'),
        },
        'ad_media_reporting_email' : {
            'level': 'INFO',
            'class': 'logging.handlers.SMTPHandler',
            'mailhost': 'smtp.postmarkapp.com',
            'credentials': (POSTMARK_API_KEY,POSTMARK_API_KEY),
            'fromaddr': 'blannon@sunlightfoundation.com',
            'toaddrs': ['jhatch@sunlightfoundation.com',
                        'blannon@sunlightfoundation.com'],
            'subject': '[Ad Hawk] New videos added',
        },
        'ad_media_reporting_log' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/ad_media_reporter.log'),
        },
        'fec_importing' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/fec_importer.log'),
        },
        'fec_kb_updating' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/fec_kb_updater.log'),
        },
        'fingerprint_ingesting' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/fingerprint_ingester.log'),
        },
        'funder_family_initializing' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/funder_family_initializer.log'),
        },
        'fec_importing' : {
                'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/fec_importer.log'),
        },
        'ie_importing' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/ie_importer.log'),
        },
        'reporting_importing' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/reporting_importer.log'),
        },
        'reporting_kb_updating' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/reporting_kb_updater.log'),
        },
        'stats_uploading' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/stats_uploader.log'),
        },
        'thumb_getting' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/thumb_getter.log'),
        },
        'video_downloading' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/video_downloader.log'),
        },
        'ftum_importing' : {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(
                LOG_ROOT,'db_script/ftum_importer.log'),
        },
        'funder_prioritizing' : {
            'level': 'INFO',
            'class': 'logging.handlers.SMTPHandler',
            'mailhost': 'smtp.postmarkapp.com',
            'credentials': (POSTMARK_API_KEY,POSTMARK_API_KEY),
            'fromaddr': 'blannon@sunlightfoundation.com',
            'toaddrs': ['jhatch@sunlightfoundation.com',
                        'blannon@sunlightfoundation.com'],
            'subject': '[Ad Hawk] New profiles needed for biggest spenders',
        },
    },
    'loggers': {
        'echoprint_server_api.fp.match' : {
            'handlers': ['matching'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'echoprint_server_api.fp.fingerprint' : {
            'handlers': ['fp_querying'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'db_script.ad_media_importer' : {
            'handlers': ['ad_media_importing'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'db_script.fec_importer' : {
            'handlers': ['fec_importing'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'db_script.fec_kb_updater' : {
            'handlers': ['fec_kb_updating'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'db_script.ie_importer' : {
            'handlers': ['ie_importing'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'db_script.ad_media_importer' : {
            'handlers': ['ad_media_importing'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'db_script.ad_media_reporter' : {
            'handlers': ['ad_media_reporting_email','ad_media_reporting_log'],
            'propagate': True,
            'level': 'INFO',
        },
        'db_script.fingerprint_ingester' : {
            'handlers': ['fingerprint_ingesting'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'db_script.funder_family_initializer' : {
            'handlers': ['funder_family_initializing'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'db_script.reporting_importer' : {
            'handlers': ['reporting_importing'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'db_script.reporting_kb_updater' : {
            'handlers': ['reporting_kb_updating'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'db_script.stats_uploader' : {
            'handlers': ['stats_uploading'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'db_script.thumb_getter' : {
            'handlers': ['thumb_getting'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'db_script.video_downloader' : {
            'handlers': ['video_downloading'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'db_script.ftum_importer' : {
            'handlers': ['ftum_importing'],
            'propagate': True,
            'level': 'DEBUG'
            },
        'db_script.funder_prioritizer' : {
            'handlers': ['funder_prioritizing'],
            'propagate': True,
            'level': 'DEBUG',
            },
    }
}

# Django debug toolbar. We can add our ip range if we end up doing debugging on production
INTERNAL_IPS = ('127.0.0.1',)
