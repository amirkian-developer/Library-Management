from django import template
from ..models import *


register=template.Library()


@register.simple_tag
def date_format(date):
    return date.strftime("%Y-%m-%d")

@register.simple_tag
def datetime_format(date):
    return date.strftime("%Y.%m.%d %H:%M")

