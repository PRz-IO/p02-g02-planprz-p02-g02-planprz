from django import template

register = template.Library()

@register.filter
def link(obraz):
    return obraz.decode("utf-8")
