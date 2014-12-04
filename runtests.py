import sys

import django

try:
    from django.conf import settings

    _settings = {
        'DEBUG': True,
        'USE_TZ': True,
        'LANGUAGE_CODE': 'en-us',
        'LANGUAGES': (
            ('en-us', 'English'),
        ),
        'DATABASES': {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'responsive',
            }
        },
        'ROOT_URLCONF': 'responsive_wrapper.urls',
        'INSTALLED_APPS': [
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.admin',
            'cms',
            'mptt',
            'menus',
            'sekizai',
            'responsive',
            'responsive_wrapper',
        ],
        'MIDDLEWARE_CLASSES': (
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',

            # django-cms
            'cms.middleware.page.CurrentPageMiddleware',
            'cms.middleware.user.CurrentUserMiddleware',
            'cms.middleware.toolbar.ToolbarMiddleware',

            'responsive.middleware.ResponsiveMiddleware', # django-responsive2
        ),
        'TEMPLATE_CONTEXT_PROCESSORS': (
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.i18n',
            'django.core.context_processors.request',
            'django.core.context_processors.media',
            'django.core.context_processors.static',
            'cms.context_processors.cms_settings',
            'sekizai.context_processors.sekizai',
            'responsive.context_processors.device', # django-responsive2
        ),
        'SITE_ID': 1,
        'SOUTH_MIGRATION_MODULES': {
            'responsive_wrapper': 'responsive_wrapper.south_migrations',
        },
        'NOSE_ARGS': ['-s'],
    }


    if django.VERSION < (1,7):
        _settings['INSTALLED_APPS'] += ['south']

    settings.configure(**_settings)
        
    try:
        setup = django.setup
    except AttributeError:
        pass
    else:
        setup()

    from django_nose import NoseTestSuiteRunner
except ImportError:
    import traceback
    traceback.print_exc()
    raise ImportError("To fix this error, run: pip install -r requirements-test.txt")


def run_tests(*test_args):
    if not test_args:
        test_args = ['tests']

    # Run tests
    test_runner = NoseTestSuiteRunner(verbosity=1)

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
