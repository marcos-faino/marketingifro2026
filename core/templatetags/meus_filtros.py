from django import template

register = template.Library()

@register.filter
def resto(value, arg):
    return int(value) % int(arg)