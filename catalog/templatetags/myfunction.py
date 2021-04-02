# create html's function
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def divice(x):
    t = x%10
    if t == 1:
        return x
