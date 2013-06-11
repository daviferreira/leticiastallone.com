from django import template

from pages.models import Page


register = template.Library()


@register.inclusion_tag('pages/partial.html')
def render_partial(slug):
    page = Page.objects.get(slug=slug)
    return {'page': page}
