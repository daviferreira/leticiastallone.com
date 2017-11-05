from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView
from django.views.generic.base import RedirectView

from filebrowser.sites import site

from blog.models import Post
from links.models import ItemLink
from presentations.models import Presentation
from publications.models import Article


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
    url(r'^publications$',
        ListView.as_view(
            queryset=Article.objects.filter(is_published=True).order_by('-pub_date'),
            context_object_name='articles',
            template_name='publications/article_list.html'
        ),
       name='publications'),
    url(r'^publication/', include('publications.urls')),
    url(r'^blog$',
        ListView.as_view(
            queryset=Post.objects.filter(is_published=True).order_by('-pub_date'),
            context_object_name='posts',
            template_name='blog/post_list.html'
        ),
       name='blog'),
    url(r'^blog/', include('blog.urls')),
    url(r'^presentations$',
        ListView.as_view(
            queryset=Presentation.objects.all().order_by('-pub_date'),
            context_object_name='presentations',
            template_name='presentations/presentation_list.html'
        ),
       name='links'),
    url(r'^links$',
        ListView.as_view(
            queryset=ItemLink.objects.all().order_by('order'),
            context_object_name='links',
            template_name='links/item_link_list.html'
        ),
       name='links'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
