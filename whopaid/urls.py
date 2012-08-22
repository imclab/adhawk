from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'whopaid.views.home', name='home'),
    # url(r'^whopaid/', include('whopaid.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$','whopaid.views.landing_page'),
    url(r'^400/','django.views.defaults.page_not_found'),
    url(r'^500/','django.views.defaults.server_error'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',include('whopaid_api.urls')),
    url(r'^troubleshooting/','whopaid.views.no_match'),
    url(r'^mailinglist/', include('spammer.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    url(r'^about/$','whopaid.views.about'),
    url(r'^ad/top/$','knowledge_base.views.top_ads'),
    url(r'^ad/top/(?P<path>.*)/$','knowledge_base.views.top_ad_select'),
    url(r'^ad/(?P<path>.*)/$','knowledge_base.views.ad_profile'),
    url(r'^search/', include('search.urls')),
    )
