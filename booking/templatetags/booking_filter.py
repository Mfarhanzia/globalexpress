from django import template

register = template.Library()


@register.filter
def subtract(value, arg):
    """Removes all values of arg from the given string"""
    return "free" if value - arg == 0 else value - arg
