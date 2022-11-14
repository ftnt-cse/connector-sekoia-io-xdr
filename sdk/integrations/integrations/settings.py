""" Copyright start
  Copyright (C) 2008 - 2020 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
"""
Django settings for connector project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Import some utility functions
import os
from os import mkdir
from os.path import abspath, basename, dirname, join, exists
from configparser import RawConfigParser

from utils.config_parser import all_config

ALL_CONFIG = all_config
# ##### PATH CONFIGURATION ################################
# Fetch Django's project directory
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Fetch the project_root
PROJECT_ROOT = dirname(DJANGO_ROOT)

# The name of the whole site
SITE_NAME = basename(DJANGO_ROOT)

# Load configurations
CONFIG_DIR = join(DJANGO_ROOT, 'configs')
CONFIG_FILE = 'config.ini'
application_config = RawConfigParser()
application_config.read(join(CONFIG_DIR, CONFIG_FILE))

# ##### APPLICATION CONFIGURATION #########################
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
]

THIRD_PARTY_APPS = [
    #'corsheaders',
]

CONNECTOR_APPS = [
    'postman',
    'connectors',
    'annotation',
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + CONNECTOR_APPS

# Middlewares
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Connector settings

CONNECTORS_DIR = join(DJANGO_ROOT, 'connectors')
CONNECTOR_DEVELOPMENT_DIR = join(DJANGO_ROOT, 'connector_development')
CONNECTOR_TEMPLATE_DIR = join(DJANGO_ROOT, 'connector_development', 'core', 'templates')
CONNECTORS_EXTENSION = '.tgz'
CONNECTOR_DEVELOPMENT_VERSION_POSTFIX = '_dev'
CONNECTORS_RESERVED = ('core', 'cyops_utilities', 'file_operations', 'database', 'imap', 'smtp', 'irc', 'soap', 'ssh', 'code-snippet', 'cyops-schedule-report', 'cyops-system-monitoring', 'bpmn-to-playbooks', 'fortisoar-ml-engine')

WEB_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'web/')
STATIC_URL = '/integration/static/'
STATIC_ROOT = join(WEB_ROOT, 'static/')

# ##### DATABASE CONFIGURATION ############################
DB_HOST = application_config.get('database', 'db_host')
DB_NAME = application_config.get('database', 'db_name')
DB_USER = application_config.get('database', 'db_user')
DB_PASSWORD = application_config.get('database', 'db_password')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'NAME': join(DJANGO_ROOT, 'data.sqlite'),
        'HOST': DB_HOST
    }
}

# ##### SECURITY CONFIGURATION ############################
SECRET_KEY = '1qsjrdu6005n=^ukpx=&_scsrf%28)4xvbo%904-8+@him6$hp'

# ##### DJANGO RUNNING CONFIGURATION ######################
# The default WSGI application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

# The root URL configuration
ROOT_URLCONF = '%s.urls' % SITE_NAME

TEMPLATES = [
    {
        'NAME': 'django',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
    {
        'NAME': 'jinja2',
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [],
        'APP_DIRS': False,
        'OPTIONS': {
            'environment': 'integrations.jinja.environment'
        }
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'connectors.pagination.ConnectorPageNumberPagination',
    'PAGE_SIZE': 30,
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

# This site's ID
SITE_ID = 1

# ##### INTERNATIONALIZATION ##############################
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

# Internationalization
USE_I18N = True

# Localization
USE_L10N = True

# enable time zone awareness by default
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = join(DJANGO_ROOT, 'static/')

TMP_FILE_ROOT = '/tmp/'

# DEBUG
DEBUG = False
if application_config.getboolean('application', 'debug'):
    DEBUG = True

# RabbitMQ Publisher
CONNECTION_RETRY_COUNT = 3
CONNECTION_RETRY_DELAY = 5
PUBLISH_MESSAGE_RETRY_COUNT = 5

ROUTER_HEARTBEAT = int(application_config.get('router', 'heartbeat'))
ROUTER_CONNECTION_ATTEMPTS = int(application_config.get('router', 'connection_attempts'))
ROUTER_RETRY_DELAY = int(application_config.get('router', 'retry_delay'))
SELF_ID = None
MASTER_ID = None


# ##### LOGGING ##############################
APP_LOG_FILE_PATH = application_config.get('logging', 'app_log_file_path')
APP_LOG_FILE_SIZE = eval(application_config.get('logging', 'app_log_file_size'))
APP_LOG_FILE_BACKUP_COUNT = eval(application_config.get('logging', 'app_log_file_backup_count'))

CONNECTOR_LOGGER_LEVEL = application_config.get('logging', 'connector_logger_level')
DJANGO_LOGGER_LEVEL = application_config.get('logging', 'django_logger_level')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(name)s %(module)s %(funcName)s(): %(message)s'
        }
    },
    'handlers': {
        'app_logger': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': APP_LOG_FILE_PATH,
            'maxBytes': APP_LOG_FILE_SIZE,
            'backupCount': APP_LOG_FILE_BACKUP_COUNT,
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'connectors': {
            'handlers': ['app_logger'],
            'level': CONNECTOR_LOGGER_LEVEL,
            'propagate': False
        },
        'postman': {
            'handlers': ['app_logger'],
            'level': CONNECTOR_LOGGER_LEVEL,
            'propagate': False
        },
        'pika': {
            'handlers': ['app_logger'],
            'level': CONNECTOR_LOGGER_LEVEL,
            'propagate': False
        },
        'django.request': {
            'handlers': ['app_logger'],
            'level': DJANGO_LOGGER_LEVEL,
            'propagate': False
        }
    }
}

CONNECTOR_TEMPLATES = []
CONNECTORS_REPO_NAMES = []
ENCRYPTION = False
LW_AGENT = True
SDK_PORT = '8000'
RELEASE_VERSION = 'dev'
ENABLE_REMOTE_CONNECTOR_OPERATION = eval(application_config.get('application', 'ENABLE_REMOTE_CONNECTOR_OPERATION',  fallback='True'))
REPLICATING_LOG = {}
LOG_PAGINATION = 100
MAX_RECORD_LIMIT = '500'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
