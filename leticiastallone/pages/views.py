# coding: utf-8
from django.conf import settings
from django.shortcuts import render_to_response
from django.views.generic.detail import DetailView

from .models import Page
from blog.models import Post


class PageDetailView(DetailView):
    model = Page
    context_object_name = 'page'

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        return context


def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-pub_date')[:3]
    return render_to_response('home.html', {
        'posts': posts,
        'STATIC_URL': settings.STATIC_URL
    }, mimetype='text/html')
