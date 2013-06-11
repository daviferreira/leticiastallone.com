from django import template
from publications.models import Article


register = template.Library()


@register.inclusion_tag('publications/publications.html')
def show_publications():
    articles = Article.objects.filter(is_published=True).order_by('-pub_date')[:2]
    return {'articles' : articles}
