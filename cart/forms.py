from django import forms
from . import models


class AddToCartForm(forms.ModelForm):
    quantity = forms.IntegerField(required=True)

    class Meta:
        model = models.CartItem
        fields = ["quantity"]
