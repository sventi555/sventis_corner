from django import template
from django.utils.safestring import mark_safe

import markdown2

from guides.models import Category


register = template.Library()


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)


@register.simple_tag('categories')
def categories():
    return Category.objects.all()
