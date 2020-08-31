from django import template
from django.forms import CheckboxInput

register = template.Library()


@register.filter(name="is_checkbox")
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__


@register.filter(name="in_list")
def in_list(value, the_list):
    value = str(value)
    return value in the_list.split(",")

