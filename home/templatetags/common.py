import unicodedata
from django import template

register = template.Library()

@register.filter
def remove_accents(value):
    nkfd_form = unicodedata.normalize('NFKD', unicode(value))
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])