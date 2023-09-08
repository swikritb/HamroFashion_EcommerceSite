from django.shortcuts import render, redirect
from django.views import View
from . import forms
from . import models
from django.db.models import Sum
from django.views.generic import DetailView
from django.urls import reverse

from django.http import HttpResponse, FileResponse
from django.views.generic import View

from .utils import render_to_pdf  # created in step 4

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


User = settings.AUTH_USER_MODEL


# Create your views here.
class CheckOutView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        if request.user.cart.items.all().count() == 0:
            messages.info(request, "Please add some items")
            return redirect("home")

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        total_price = (
            request.user.cart.items.all().aggregate(Sum("price"))["price__sum"] or 0
        )

        try:
            profile = models.CheckoutProfile.objects.get(user=request.user)
            if profile is not None:
                checkout_form = forms.CheckOutForm(
                    initial={
                        "phone_no": profile.phone_no,
                        "address": profile.address,
                        "email": profile.email,
                    }
                )
        except Exception as e:
            checkout_form = forms.CheckOutForm(initial={"email": request.user})

        return render(
            request,
            "orders/checkout.html",
            {
                "checkout_form": checkout_form,
                "total_price": int(total_price),
                "KHALTI_PUBLIC_KEY": "live_secret_key_68791341fdd94846a146f0457ff7b455",
            },
        )

    def post(self, request):
        total_price = (
            request.user.cart.items.all().aggregate(Sum("price"))["price__sum"] or 0
        )
        # checkout form
        data = request.POST
        discount = 0

        if not request.POST.get("KHALTI_TRANSACTION_CODE"):
            messages.add_message(
                request, messages.ERROR, "Invalid khalti transaction code"
            )

        

        checkout_form = forms.CheckOutForm(request.POST)
        if checkout_form.is_valid():
            """
            Make an order objects whose cart objects
            cart object is same as that of request.user
            pop out the cart items and
            """
            messages.add_message(
                request, messages.ERROR, "Order received, thankyou"
            )
            cart = request.user.cart
            checkout_form_data = checkout_form.save(commit=False)

            total_price = cart.items.all().aggregate(Sum("price"))["price__sum"]

            print(checkout_form_data)

            order = models.Order(
                initial_price=total_price,
                address=checkout_form_data.address,
                phone_no=checkout_form_data.phone_no,
                user=request.user,
                discount_amount=discount * total_price,
                total_price=total_price - (discount * total_price),
                email=request.user.email,
            )

            order.save()

            request.user.cart.items.all().update(belongs_to_order=True)
            order.items.add(*request.user.cart.items.all())

            # lets clean user off his old cart
            request.user.cart.items.clear()

            return redirect(reverse("order", kwargs={"url_code": order.url_code}))


class DetailViewOrder(DetailView):
    model = models.Order
    slug_field = "url_code"
    slug_url_kwarg = "url_code"
    template_name = "orders/view_order.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = f"{data['object'].user} - Order"
        return data
