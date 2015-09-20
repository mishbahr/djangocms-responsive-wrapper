=============================
djangocms-responsive-wrapper
=============================

.. image:: http://img.shields.io/pypi/v/djangocms-responsive-wrapper.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-responsive-wrapper/
    :alt: Latest Version

.. image:: http://img.shields.io/pypi/dm/djangocms-responsive-wrapper.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-responsive-wrapper/
    :alt: Downloads

.. image:: http://img.shields.io/pypi/l/djangocms-responsive-wrapper.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-responsive-wrapper/
    :alt: License


This projects integrates `django-responsive2 <https://github.com/mishbahr/django-responsive2>`_ with `django-cms >= 3.0 <https://github.com/divio/django-cms/>`_

This django CMS plugin will allow a site editor to display different contents based on breakpoints. For a more detailed description and reasoning behind this concept, please read the project description for ``django-responsive2.``

This project requires ``django-responsive2`` and ``django-cms`` v3.0 or higher to be properly installed and configured. When installing the ``djangocms-responsive-wrapper`` using pip, ``django-responsive2`` will also be installed automatically.

The full documentation for ``django-responsive2`` is available at https://django-responsive2.readthedocs.org.



Quickstart
----------

1. Install ``djangocms-responsive-wrapper``::

    pip install djangocms-responsive-wrapper

2. Add ``responsive_wrapper`` to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'responsive_wrapper',
        ...
    )

AJAX load plugin based on window size
-------------------------------------
By default, ``responsive_wrapper`` renders the plugins based on device dimensions.

However, if you would like the plugin to use the window size to render the plugin, set the ``RESPONSIVE_WRAPPER_TEMPLATE`` to use an alternate template::

    RESPONSIVE_WRAPPER_TEMPLATE = 'responsive_wrapper/live_reload.html'

And add the ``responsive_wrapper.urls`` to your project's ``urls`` module or create a django CMS page to hook the application into. In ``Advanced Settings``, set its Application to ``Responsive Wrapper`` (this requires a server restart)::

    urlpatterns = patterns(
        ...
        url(r'^responsive/', include('responsive_wrapper.urls')),
        ...
    )

The ``ResponsiveWrapper.js``, included in the ``live_reload.html`` triggers a ``replace`` event when the content has been replaced. This can be useful when you want to change some styles  or reinitialize any JavaScript on your page based on which content is loaded.

Configuration
-------------

Plugin(s) Module::

    RESPONSIVE_WRAPPER_MODULE = _('Generic')

Name of the plugin::

    RESPONSIVE_WRAPPER_NAME = _('Responsive Wrapper')

The path to the template used to render the template::

    RESPONSIVE_WRAPPER_TEMPLATE = 'responsive_wrapper/default.html'

Can the plugin be inserted inside the text plugin?
::

    RESPONSIVE_WRAPPER_TEXT_ENABLED = False

Can this plugin only be attached to a placeholder that is attached to a page?::

    RESPONSIVE_WRAPPER_PAGE_ONLY = False

A List of Plugin Class Names. If this is set, only plugins listed here can be added to this plugin::

    RESPONSIVE_WRAPPER_CHILD_CLASSES = None

Is it required that this plugin is a child of another plugin? Or can it be added to any placeholder::

    RESPONSIVE_WRAPPER_REQUIRE_PARENT = False

A list of Plugin Class Names. If this is set, this plugin may only be added to plugins listed here::

    RESPONSIVE_WRAPPER_PARENT_CLASSES = None

Set fieldsets to control the layout of plugin “add” and “change” form::

    RESPONSIVE_WRAPPER_FIELDSETS = None


You may also like...
--------------------

* djangocms-disqus - https://github.com/mishbahr/djangocms-disqus
* djangocms-forms — https://github.com/mishbahr/djangocms-forms
* djangocms-gmaps — https://github.com/mishbahr/djangocms-gmaps
* djangocms-instagram — https://github.com/mishbahr/djangocms-instagram
* djangocms-twitter2 — https://github.com/mishbahr/djangocms-twitter2
* djangocms-youtube — https://github.com/mishbahr/djangocms-youtube
