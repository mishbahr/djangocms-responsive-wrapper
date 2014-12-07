=============================
djangocms-responsive-wrapper 
=============================

.. image:: http://img.shields.io/travis/mishbahr/djangocms-responsive-wrapper.svg?style=flat-square
    :target: https://travis-ci.org/mishbahr/djangocms-responsive-wrapper/

.. image:: http://img.shields.io/pypi/v/djangocms-responsive-wrapper.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-responsive-wrapper/
    :alt: Latest Version

.. image:: http://img.shields.io/pypi/dm/djangocms-responsive-wrapper.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-responsive-wrapper/
    :alt: Downloads

.. image:: http://img.shields.io/pypi/l/djangocms-responsive-wrapper.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-responsive-wrapper/
    :alt: License

.. image:: http://img.shields.io/coveralls/mishbahr/djangocms-responsive-wrapper.svg?style=flat-square
  :target: https://coveralls.io/r/mishbahr/djangocms-responsive-wrapper?branch=master

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

Configuration
-------------

These are the list of options that can be overridden for this plugin. Please refer to django-cms documentation for full details:

 
http://django-cms.readthedocs.org/en/latest/extending_cms/custom_plugins.html 


------------

``RESPONSIVE_WRAPPER_MODULE``

Default: ``Generic``

------------

``RESPONSIVE_WRAPPER_NAME``

Default: ``Responsive Wrapper``

------------

``RESPONSIVE_WRAPPER_TEMPLATE``

The path to the template used to render the template. 

Default: ``'responsive_wrapper/default.html'``

------------

``RESPONSIVE_WRAPPER_TEXT_ENABLED``

Can the plugin be inserted inside the text plugin?

Default: ``False``

------------

``RESPONSIVE_WRAPPER_PAGE_ONLY``

Can this plugin only be attached to a placeholder that is attached to a page?

Default: ``False``

------------

``RESPONSIVE_WRAPPER_CHILD_CLASSES``

A List of Plugin Class Names. If this is set, only plugins listed here can be added to this plugin

Default: ``None``

------------

``RESPONSIVE_WRAPPER_REQUIRE_PARENT``

Is it required that this plugin is a child of another plugin? Or can it be added to any placeholder.

Default: ``False``

------------

``RESPONSIVE_WRAPPER_PARENT_CLASSES``

A list of Plugin Class Names. If this is set, this plugin may only be added to plugins listed here.

Default: ``None``

------------

``RESPONSIVE_WRAPPER_FIELDSETS``

Set fieldsets to control the layout of plugin “add” and “change” form.

Default: ``None``
