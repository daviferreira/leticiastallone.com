from django.conf.urls import patterns, url

from publications.views import ArticleDetailView


urlpatterns = patterns('',
    url(r'article/(?P<slug>[-_\w]+)\.html$', ArticleDetailView.as_view(), name='article-detail'),
)
