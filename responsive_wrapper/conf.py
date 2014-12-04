from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _

from appconf import AppConf


class ResponsiveWrapperConf(AppConf):
    CACHE = getattr(settings, 'CMS_PLUGIN_CACHE', True)
    CHILD_CLASSES = None
    FIELDSETS = None
    MODULE = _('Generic')
    NAME = _('Responsive Wrapper')
    PAGE_ONLY = False
    PARENT_CLASSES = None
    REQUIRE_PARENT = False
    TEMPLATE = 'responsive_wrapper/default.html'
    TEXT_ENABLED = False

    class Meta:
        prefix = 'responsive_wrapper'
