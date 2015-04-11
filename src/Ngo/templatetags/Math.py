import os
from django import template
register = template.Library()

@register.filter(name='sub')
def sub(f, s):
    return s-f
