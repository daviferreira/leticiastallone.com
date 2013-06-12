from django import template
from links.models import ItemLink


register = template.Library()


@register.inclusion_tag('links/highlighted_links.html')
def show_highlighted_links():
    itens = ItemLink.objects.filter(highlight=True).order_by('order')
    return {'itens' : itens}
