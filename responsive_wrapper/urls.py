from django.conf.urls import patterns, url

from .views import ajax_render

urlpatterns = patterns(
    '',
    url(r'^render/(?P<plugin_id>[-\w]+)/$', ajax_render, name='ajax-render')
)
