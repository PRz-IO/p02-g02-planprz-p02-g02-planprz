from django import template

register = template.Library()

@register.filter
def in_id(things, id):
    return things.filter(dni_tygodnia_id_dnia_tygodnia=id)

@register.filter
def get_att(things):
    return getattr(things, 'godz_otw')