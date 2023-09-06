from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, mixins
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.http import QueryDict
from django.views import View
from . import forms
from orders.models import Order, User, CheckoutProfile


class Login(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")

        return super(Login, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        # login form
        lform = forms.UserLoginForm()
        if request.GET.get("next"):
            messages.info(request, "Please login")
        return render(
            request, "users/login.html", context={"lform": lform, "val": "Log In"}
        )

    def post(self, request):
        lform = forms.UserLoginForm(request.POST)
        if lform.is_valid():
            user = authenticate(
                request,
                email=lform.cleaned_data.get("email"),
                password=lform.cleaned_data.get("password"),
            )
            if user is not None:
                login(request, user)
                messages.info(request, f"{user.email} account logged in")

                if request.POST.get("next"):
                    return redirect(request.POST.get("next"))
                else:
                    return redirect(settings.LOGIN_REDIRECT_URL)

        messages.info(request, "Wrong Credentials")
        return render(
            request, "users/login.html", context={"lform": lform, "val": "Log In"}
        )


class Signup(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super(Signup, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        # signin form
        sform = forms.UserAdminCreationForm()
        return render(request, "users/login.html", {"lform": sform, "val": "Sign In"})

    def post(self, request):
        sform = forms.UserAdminCreationForm(request.POST)
        if sform.is_valid():
            user = sform.save(commit=True)
            messages.info(request, f"{user.email} account created")
            return redirect("login")

        return render(request, "users/login.html", {"lform": sform, "val": "Sign In"})


# Create your views here.


def logout_user(request):
    if request.user.is_authenticated:
        user = str(request.user)
        logout(request)
        messages.info(request, f"Successfully logged out of {user}")
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return redirect("home")
