from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'colourlens.views',
    url(r'^$', 'index', name='index'),

    url(r'^ajax/artworks/$', 'artwork_list', name='artwork_list'),
    url(r'^ajax/artwork/(\w+)/$', 'artwork_info', name='artwork_info'),
)
