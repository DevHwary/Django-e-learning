from django import template



''' Django doesn't allow accessing
variables or attributes starting with an underscore in templates to prevent retrieving
private attributes or calling private methods. You can solve this by writing a custom
template filter.
'''

register = template.Library()

@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None
