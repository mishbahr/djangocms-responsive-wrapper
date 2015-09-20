#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import responsive_wrapper

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = responsive_wrapper.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()

setup(
    name='djangocms-responsive-wrapper',
    version=version,
    description="""This projects integrates django-responsive2 with django-cms >= 3.0""",
    long_description=readme,
    author='Mishbah Razzaque',
    author_email='mishbahx@gmail.com',
    url='https://github.com/mishbahr/djangocms-responsive-wrapper',
    packages=[
        'responsive_wrapper',
    ],
    include_package_data=True,
    install_requires=[
        'django-appconf',
        'django-cms>=3.0',
        'django-responsive2',
        'hashids',
    ],
    license="BSD",
    zip_safe=False,
    keywords='djangocms-responsive-wrapper, django-responsive2, django-cms',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
