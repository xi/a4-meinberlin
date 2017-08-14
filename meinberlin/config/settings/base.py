"""
Django settings for meinberlin project.

Generated by 'django-admin startproject' using Django 1.8.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

CONFIG_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(CONFIG_DIR)
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
    'wagtail.contrib.wagtailstyleguide',

    'taggit',  # wagtail dependency
    'widget_tweaks',
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rules.apps.AutodiscoverRulesConfig',
    'easy_thumbnails',
    'ckeditor',
    'ckeditor_uploader',
    'capture_tag',
    'background_task',

    'adhocracy4.organisations.apps.OrganisationsConfig',
    'adhocracy4.projects.apps.ProjectsConfig',
    'adhocracy4.images.apps.ImagesConfig',
    'adhocracy4.phases.apps.PhasesConfig',
    'adhocracy4.modules.apps.ModulesConfig',
    'adhocracy4.ratings.apps.RatingsConfig',
    'adhocracy4.reports.apps.ReportsConfig',
    'adhocracy4.comments.apps.CommentsConfig',
    'adhocracy4.categories.apps.CategoriesConfig',
    'adhocracy4.maps.apps.MapsConfig',
    'adhocracy4.actions.apps.ActionsConfig',
    'adhocracy4.follows.apps.FollowsConfig',
    'adhocracy4.filters.apps.FiltersConfig',

    'meinberlin.apps.contrib.apps.Config',
    'meinberlin.apps.cms.apps.Config',
    'meinberlin.apps.users.apps.Config',
    'meinberlin.apps.projects.apps.Config',
    'meinberlin.apps.modules.apps.Config',
    'meinberlin.apps.organisations.apps.Config',
    'meinberlin.apps.embed.apps.Config',
    'meinberlin.apps.moderatorfeedback.apps.Config',
    'meinberlin.apps.maps.apps.Config',
    'meinberlin.apps.notifications.apps.Config',
    'meinberlin.apps.exports.apps.Config',
    'meinberlin.apps.offlineevents.apps.Config',
    'meinberlin.apps.newsletters.apps.Config',

    'meinberlin.apps.account.apps.Config',
    'meinberlin.apps.dashboard.apps.Config',
    'meinberlin.apps.dashboard2.apps.Config',
    'meinberlin.apps.initiators.apps.Config',

    'meinberlin.apps.actions.apps.Config',
    'meinberlin.apps.bplan.apps.Config',
    'meinberlin.apps.budgeting.apps.Config',
    'meinberlin.apps.documents.apps.Config',
    'meinberlin.apps.extprojects.apps.Config',
    'meinberlin.apps.ideas.apps.Config',
    'meinberlin.apps.kiezkasse.apps.Config',
    'meinberlin.apps.mapideas.apps.Config',
    'meinberlin.apps.polls.apps.Config',
    'meinberlin.apps.topicprio.apps.Config',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',

    'meinberlin.apps.embed.middleware.AjaxPathMiddleware',
)

SITE_ID = 1

ROOT_URLCONF = 'meinberlin.config.urls'

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'meinberlin.config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

IMAGE_ALIASES = {
    '*': {
        'max_size': 5*10**6,
        'fileformats': ('image/png', 'image/jpeg', 'image/gif')
    },
    'heroimage': {'min_resolution': (1500, 500)},
    'tileimage': {'min_resolution': (500, 300)},
    'logo': {'min_resolution': (200, 50)},
    'avatar': {'min_resolution': (200, 200)},
    'idea_image': {'min_resolution': (800, 200)},
}

THUMBNAIL_ALIASES = {
    '': {
        'heroimage': {'size': (1500, 500), 'crop': 'smart'},
        'heroimage_preview': {'size': (880, 220), 'crop': 'smart'},
        'project_thumbnail': {'size': (520, 330), 'crop': 'smart'},
        'idea_image': {'size': (800, 0), 'crop': 'scale'},
        'idea_thumbnail': {'size': (240, 240), 'crop': 'smart'},
    }
}

ALLOWED_UPLOAD_IMAGES = ('png', 'jpeg', 'gif')


# Wagtail settings

WAGTAIL_SITE_NAME = 'meinberlin'

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://localhost:8000'

# Authentication

AUTH_USER_MODEL = 'meinberlin_users.User'

AUTHENTICATION_BACKENDS = (
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_ADAPTER = 'meinberlin.apps.users.adapters.AccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300  # seconds
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_SIGNUP_FORM_CLASS = 'meinberlin.apps.users.forms.TermsSignupForm'
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'

LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',  # a3
    'meinberlin.apps.users.hashers.A2PasswordHasher',
]

# Service Konto
SERVICE_KONTO_LOGIN_URL = 'https://skbref.verwalt-berlin.de/skb/FVS/Login/Anmeldung.aspx'
SERVICE_KONTO_HELP_URL = 'https://skbref.verwalt-berlin.de/skb/FVP/FV/BasisHilfe/HilfeIndex.aspx'
SERVICE_KONTO_API_URL = 'https://skbref.verwalt-berlin.de/HHGWUserData/HHGWUserData.asmx?wsdl'

# ckeditor

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_RESTRICT_BY_USER = 'username'
CKEDITOR_ALLOW_NONIMAGE_FILES = True

CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink']
        ]
    },
    'image-editor': {
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Image'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink']
        ]
    }
}

BLEACH_LIST = {
    'default' : {
        'tags': ['p','strong','em','u','ol','li','ul','a'],
        'attributes': {
            'a': ['href', 'rel'],
        },
    },
    'image-editor': {
        'tags': ['p','strong','em','u','ol','li','ul','a','img'],
        'attributes': {
            'a': ['href', 'rel'],
            'img': ['src', 'alt', 'style']
        },
        'styles': [
            'float',
            'margin',
            'padding',
            'width',
            'height',
            'margin-bottom',
            'margin-top',
            'margin-left',
            'margin-right',
        ],
    }
}


# adhocracy4

A4_ORGANISATIONS_MODEL = 'meinberlin_organisations.Organisation'

A4_RATEABLES = (
    ('a4comments', 'comment'),
    ('meinberlin_ideas', 'idea'),
    ('meinberlin_mapideas', 'mapidea'),
    ('meinberlin_budgeting', 'proposal'),
    ('meinberlin_topicprio', 'topic'),
    ('meinberlin_kiezkasse', 'proposal'),
)

A4_COMMENTABLES = (
    ('a4comments', 'comment'),
    ('meinberlin_ideas', 'idea'),
    ('meinberlin_documents', 'chapter'),
    ('meinberlin_documents', 'paragraph'),
    ('meinberlin_mapideas', 'mapidea'),
    ('meinberlin_budgeting', 'proposal'),
    ('meinberlin_topicprio', 'topic'),
    ('meinberlin_polls', 'poll'),
    ('meinberlin_kiezkasse', 'proposal'),
)

A4_REPORTABLES = (
    ('a4comments', 'comment'),
    ('meinberlin_ideas', 'idea'),
    ('meinberlin_mapideas', 'mapidea'),
    ('meinberlin_budgeting', 'proposal'),
    ('meinberlin_topicprio', 'topic'),
    ('meinberlin_kiezkasse', 'proposal'),
)

A4_ACTIONABLES = (
    ('a4comments', 'comment'),
    ('meinberlin_ideas', 'idea'),
    ('meinberlin_mapideas', 'mapidea'),
    ('meinberlin_budgeting', 'proposal'),
    ('meinberlin_kiezkasse', 'proposal'),
)

A4_AUTO_FOLLOWABLES = (
    ('a4comments', 'comment'),
    ('meinberlin_ideas', 'idea'),
    ('meinberlin_mapideas', 'mapidea'),
    ('meinberlin_budgeting', 'proposal'),
    ('meinberlin_kiezkasse', 'proposal'),
    ('meinberlin_polls', 'vote'),  # TODO: really?
)

A4_MAP_BASEURL = 'https://maps.berlinonline.de/tile/bright/'
A4_MAP_ATTRIBUTION = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
A4_MAP_BOUNDING_BOX = ([[52.3517, 13.8229], [52.6839, 12.9543]])

CONTACT_EMAIL = 'support-berlin@liqd.de'
EMAIL_DEFAULT_LANGUAGE = 'de'
