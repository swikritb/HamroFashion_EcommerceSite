from django import forms
from . import models


class CheckOutForm(forms.ModelForm):
    address = forms.CharField(
        max_length=40,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Your billing/dropping address"}),
        help_text="where should we drop your item",
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Your Email Address"}),
        help_text="A confirmation will arrive to you. Check your mail",
    )

    phone_no = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={"placeholder": "Your phone number"}),
        help_text="We might contact you",
        required=True,
    )

    message = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Message to the Deleivery guy. Try providing some landmarks about the provided address like banks, housings, etc."
            }
        ),
    )

    class Meta:
        model = models.CheckoutProfile
        exclude = ["user", "cdate"]
