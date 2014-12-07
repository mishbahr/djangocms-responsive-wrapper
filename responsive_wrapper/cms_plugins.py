from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from django.utils import six
from django.utils.safestring import mark_safe

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .conf import settings
from .forms import ResponsiveWrapperForm
from .models import ResponsiveWrapper


class ResponsiveWrapperPlugin(CMSPluginBase):
    model = ResponsiveWrapper
    form = ResponsiveWrapperForm
    allow_children = True
    cache = False

    render_template = settings.RESPONSIVE_WRAPPER_TEMPLATE
    name = settings.RESPONSIVE_WRAPPER_NAME
    module = settings.RESPONSIVE_WRAPPER_MODULE
    
    text_enabled = settings.RESPONSIVE_WRAPPER_TEXT_ENABLED
    page_only = settings.RESPONSIVE_WRAPPER_PAGE_ONLY
    child_classes = settings.RESPONSIVE_WRAPPER_CHILD_CLASSES
    require_parent = settings.RESPONSIVE_WRAPPER_REQUIRE_PARENT
    parent_classes = settings.RESPONSIVE_WRAPPER_PARENT_CLASSES

    def render(self, context, instance, placeholder):
        context = super(ResponsiveWrapperPlugin, self).render(context, instance, placeholder)
        device = getattr(context['request'], settings.RESPONSIVE_VARIABLE_NAME, None)
        if not device:
            raise ImproperlyConfigured(
                "You must enable the 'ResponsiveMiddleware'. Edit your "
                "MIDDLEWARE_CLASSES setting to insert"
                "the 'responsive.middleware.ResponsiveMiddleware'")

        render_child_plugins = False
        for name, value in six.iteritems(instance.media_queries):
            if value is True and name in device.matched:
                render_child_plugins = True

        context['render_child_plugins'] = render_child_plugins
        return context

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        form = context['adminform'].form
        adminform = admin.helpers.AdminForm(
            form,
            settings.RESPONSIVE_WRAPPER_FIELDSETS or [(None, {'fields': form.fields.keys()})],
            self.prepopulated_fields
        )
        media = mark_safe(self.media + adminform.media)
        context.update(adminform=adminform, media=media)
        return super(ResponsiveWrapperPlugin, self).render_change_form(
            request, context, add, change, form_url, obj)


plugin_pool.register_plugin(ResponsiveWrapperPlugin)
