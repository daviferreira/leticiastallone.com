from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from filebrowser.sites import site


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'pages.views.home', name='home'),
    url(r'^index\.html?$', RedirectView.as_view(url='/'), name='index'),

    # Examples:
    # url(r'^$', 'leticiastallone.views.home', name='home'),
    # url(r'^leticiastallone/', include('leticiastallone.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Grapelli admin interface
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),

    # Local apps
    url(r'^page/', include('pages.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
