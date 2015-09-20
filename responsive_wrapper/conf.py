from appconf import AppConf

from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _


class ResponsiveWrapperConf(AppConf):
    CHILD_CLASSES = None
    FIELDSETS = None
    MODULE = _('Generic')
    NAME = _('Responsive Wrapper')
    PAGE_ONLY = False
    PARENT_CLASSES = None
    REQUIRE_PARENT = False
    TEMPLATE = 'responsive_wrapper/default.html'
    TEXT_ENABLED = False

    HASHIDS_SALT = settings.SECRET_KEY

    class Meta:
        prefix = 'responsive_wrapper'
