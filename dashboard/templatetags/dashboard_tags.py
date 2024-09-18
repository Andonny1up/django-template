""" Custom template tags for the dashboard app. 
    Etiquetas de plantilla personalizadas para la aplicación de panel de control.
"""

from django import template
from ..models import Menu
from django.urls import reverse, NoReverseMatch

register = template.Library()

@register.inclusion_tag('dashboard/components/menu.html')
def render_menu(menu_name, path):
    """ Render menus, render menu for dahsboard """
    try:
        menu = Menu.objects.get(name=menu_name)
        menu_items = menu.items.filter(parent__isnull=True).order_by('order')
        return {'menu': menu_items , 'path': path}
    except Menu.DoesNotExist:
        return {'menu': None}
    

@register.simple_tag
def resolve_url(item):
    """ Resuelve la URL de un elemento de menú, ya sea dinámica o estática """
    if item.is_dynamic:
        try:
            return reverse(item.url)
        except NoReverseMatch:
            return '#'
    else:
        return item.url