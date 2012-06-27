from django.conf import settings
from django.conf.urls import patterns, include, url
from website_showroom.feeds import RssFeed

from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rss/$', RssFeed()), 
    url(r'^search/', include('haystack.urls')),

    url(r'^$', 'website_showroom.views.index'),
    url(r'^contact/', 'website_showroom.views.contact'),
    url(r'^(?P<url_name>[-\w]+)/$', 'website_showroom.views.category')
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )