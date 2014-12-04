# -*- coding: utf-8 -*-
from django.utils.encoding import force_text

try:
    import json
except ImportError:
    from django.utils import simplejson as json

from django.utils import six
from django.utils.encoding import python_2_unicode_compatible
from cms.models.pluginmodel import CMSPlugin

from .conf import settings
from .fields import JSONField


@python_2_unicode_compatible
class ResponsiveWrapper(CMSPlugin):
    media_queries = JSONField(editable=False)

    def __str__(self):
        media_queries = []
        for name, value in six.iteritems(self.media_queries):
            if value:
                try:
                    config = settings.RESPONSIVE_MEDIA_QUERIES[name]
                except KeyError:
                    pass
                else:
                    media_queries.append(
                        force_text(config.get('verbose_name', name.replace('_', ' ').title()))
                    )
        if len(media_queries) > 1:
            return u'Visible on {0} and {1}.'.format(
                ', '.join(media_queries[:-1]), media_queries[-1])
        elif media_queries:
            return u'Visible on {0}.'.format(media_queries[0])
