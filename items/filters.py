import django_filters

from django import forms
from . import models


class ItemFilter(django_filters.FilterSet):
    name = django_filters.filters.CharFilter(
        widget=forms.TextInput(attrs={"placeholder": "Search Product by Name"})
    )

    class Meta:
        model = models.Item
        fields = {
            "name": ["icontains"],
            "price": ["gt", "lt"]
        }
