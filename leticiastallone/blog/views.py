# coding: utf-8
from django.views.generic.detail import DetailView

from .models import Post


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context
