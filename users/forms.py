from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from . import models
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Column,
    Row,
)

User = models.User


class RegisterForm(UserCreationForm):
    password = forms.CharField(
        max_length=50,
        min_length=8,
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password"}),
    )
    password2 = forms.CharField(
        max_length=50,
        min_length=8,
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"}),
    )

    class Meta:
        model = models.User
        fields = (
            "email",
            "phone",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class DateInput(forms.DateInput):
    input_type = "date"


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = (
            "email",
            "phone",
        )

    field_order = [
        "email",
        "phone",
        "password1",
        "password2",
    ]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = models.User
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "phone",
            "is_active",
            "is_admin",
        )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Enter email address"}),
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={"placeholder": "Enter password"}),
    )


class UserProfileChangeForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column("email", css_class="form-group col-12 col-lg-10"),
            ),
            Row(
                Column("first_name", css_class="form-group col-12 col-md-6 col-lg-5"),
                Column("last_name", css_class="form-group col-12 col-md-6 col-lg-5"),
            ),
            Row(Column("phone", css_class="form-group col-12 col-lg-10")),
            Row(Column()),
        )
