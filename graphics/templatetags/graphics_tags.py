from django import template

register = template.Library()


@register.filter
def isolate_name(value):
    end_index = value.index('.')
    start_index = end_index
    while value[start_index] != '/':
        start_index -= 1
    return value[start_index + 1:end_index]
