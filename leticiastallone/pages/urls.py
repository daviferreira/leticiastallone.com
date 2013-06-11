from django.conf.urls import patterns, url

from pages.views import PageDetailView


urlpatterns = patterns('',
    url(r'(?P<slug>[-_\w]+)\.html$', PageDetailView.as_view(), name='page-detail'),
)
