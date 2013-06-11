from django import template
from menu.models import ItemMenu


register = template.Library()


@register.inclusion_tag('menu/menu.html')
def show_menu():
    itens = ItemMenu.objects.all().order_by('order')
    return {'itens' : itens}
