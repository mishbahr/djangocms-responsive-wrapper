from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class ResponsiveWrapperApphook(CMSApp):
    name = _('Responsive Wrapper')
    urls = ['responsive_wrapper.urls']

apphook_pool.register(ResponsiveWrapperApphook)
