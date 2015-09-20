from django.core.exceptions import FieldError
from django.http import HttpResponseNotFound
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.utils.plugins import build_plugin_tree, downcast_plugins

from .utils import hashid_to_int


def render_plugin(request, plugin_id, template_name='responsive_wrapper/render_plugin.html'):
    try:
        instance = CMSPlugin.objects.get(pk=hashid_to_int(plugin_id))
    except CMSPlugin.DoesNotExist:
        msg = _('Plugin not found.')
        return HttpResponseNotFound(force_text(msg))

    try:
        # django CMS 3-
        descendants = instance.get_descendants(include_self=True) \
            .order_by('placeholder', 'tree_id', 'level', 'position')
    except (FieldError, TypeError):
        # django CMS 3.1+
        descendants = instance.get_descendants().order_by('path')

    plugins = [instance] + list(descendants)
    plugins = downcast_plugins(plugins)
    plugins[0].parent_id = None
    plugins = build_plugin_tree(plugins)

    context = RequestContext(request)
    context['plugins'] = plugins
    return render_to_response(template_name, {}, context)
