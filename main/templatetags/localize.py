from django import template
from django.conf import settings
 
register = template.Library()
from django.utils.safestring import mark_safe
@register.simple_tag()
def localize(data, key, lang):
    try:
        option = key + '_' + lang
        response = getattr(data,option)
    except Exception as e:
        response = 'Undefined'
    return mark_safe(response)



register.filter('localize', localize)