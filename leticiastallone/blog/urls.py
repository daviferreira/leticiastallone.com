from django.conf.urls import patterns, url

from blog.views import PostDetailView


urlpatterns = patterns('',
    url(r'post/(?P<slug>[-_\w]+)\.html$', PostDetailView.as_view(), name='post-detail'),
)
