from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'', include('home.urls', namespace='home')),
                       url(r'', include('rsvp.urls', namespace='rsvp')),
                       url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                                }),
                            url(r'favicon.ico$', 'django.views.static.serve', {
                                'path': 'static/content/favicon.ico',
                                'document_root': settings.PROJECT_ROOT,
                                }),
                            )
