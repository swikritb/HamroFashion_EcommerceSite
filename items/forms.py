from . import models
from django import forms


class ReviewForm(forms.ModelForm):
    body = forms.CharField(
        max_length=400,
        required=False,
        widget=forms.Textarea(attrs={"placeholder": "Write an honest review"}),
    )

    class Meta:
        model = models.Review
        exclude = ["item", "user", "rdate"]


class ReviewReplyForm(forms.ModelForm):
    body = forms.CharField(
        max_length=400,
        required=True,
        widget=forms.Textarea(attrs={"placeholder": "Write a reply"}),
    )

    class Meta:
        model = models.ReviewReply
        fields = ["body"]
