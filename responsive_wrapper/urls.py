from django.conf.urls import patterns, url

from .views import render_plugin

urlpatterns = patterns(
    '',
    url(r'^render/(?P<plugin_id>[-\w]+)/$', render_plugin, name='render-plugin')
)
