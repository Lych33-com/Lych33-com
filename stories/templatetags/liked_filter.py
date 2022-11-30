
from django import template
  
register = template.Library()
  
@register.filter()
def liked(queryset, user):
    for like in queryset:
        if user == like.user:
            return True
    return False