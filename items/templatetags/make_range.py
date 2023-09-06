# for making range in the django template

from django.db.models import Sum, Avg
from django import template
from .. import models

register = template.Library()


@register.filter(name="fix_percent")
def fix_percent(value):
    value = float(value)
    return value * 100


@register.filter(name="get_quantity")
def get_quantity(instance):
    try:
        total_items = instance.items.all().aggregate(Sum("quantity"))
        count = total_items["quantity__sum"] or 0
    except:
        count = 0
    return count
