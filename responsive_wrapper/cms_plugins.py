from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from django.utils import six
from django.utils.safestring import mark_safe

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from responsive.utils import Device

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
        request = context.get('request', None)

        device = getattr(request, settings.RESPONSIVE_VARIABLE_NAME, None)
        if not device:
            raise ImproperlyConfigured(
                "You must enable the 'ResponsiveMiddleware'. Edit your "
                "MIDDLEWARE_CLASSES setting to insert"
                "the 'responsive.middleware.ResponsiveMiddleware'")

        if request.is_ajax():
            device_info = {
                'width': request.GET.get('width', device.width),
                'height': request.GET.get('width', device.height),
                'pixel_ratio': request.GET.get('dpr', device.pixel_ratio),
            }
            device = Device(**device_info)

        context[settings.RESPONSIVE_VARIABLE_NAME] = device

        matched_media_query = False
        for name, value in six.iteritems(instance.media_queries):
            if value is True and name in device.matched:
                matched_media_query = True

        context['matched_media_query'] = matched_media_query
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
