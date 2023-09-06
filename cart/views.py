from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum
from . import forms
from django.http import JsonResponse
import json
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class AddToCart(LoginRequiredMixin, View):
    def post(self, request):
        data = json.loads(request.body)
        add_to_cart_form = forms.AddToCartForm(data)

        id = int(data.get("itemId"))
        quantity = int(data.get("quantity"))

        # item to add
        item = models.Item.objects.get(id=id)

        if add_to_cart_form.is_valid():
            try:
                # the item in the cart
                cartItem = models.CartItem.objects.get(
                    item__id=item.id,
                    user=request.user,
                    belongs_to_order=False,
                )

                cartItem.quantity = cartItem.quantity + quantity
                cartItem.price = item.real_time_price * cartItem.quantity
                cartItem.save()

                request.user.cart.items.add(cartItem)

            except models.CartItem.DoesNotExist:
                # the item is not in the cart so
                # we need to make the cart item
                # and insert it into the cart
                cartItem = models.CartItem(
                    item=item,
                    quantity=quantity,
                    user=request.user,
                    price=item.real_time_price,
                    belongs_to_order=False,
                )
                cartItem.save()
                request.user.cart.items.add(cartItem)

            return JsonResponse(
                {
                    "result": "added to cart",
                    "count": request.user.cart.items.all().aggregate(Sum("quantity"))[
                        "quantity__sum"
                    ],
                }
            )


class RemoveFromCart(LoginRequiredMixin, View):
    def post(self, request):
        data = json.loads(request.body)
        cart = request.user.cart
        item = data.get("cart_item_id") or None
        item = models.CartItem.objects.get(id=item)
        cart.items.remove(item)
        item.delete()
        return JsonResponse(
            {
                "result": "removed",
                "count": request.user.cart.items.all().aggregate(Sum("quantity"))[
                    "quantity__sum"
                ],
            }
        )


class ClearCart(LoginRequiredMixin, View):
    def get(self, request):
        request.user.cart.items.all().delete()
        return redirect("cart")


class ViewCart(LoginRequiredMixin, View):
    def get(self, request):
        if request.GET.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            resp = []
            for item in request.user.cart.items.all():
                resp.append(item.to_json())
            return JsonResponse(
                {
                    "res": resp,
                    "total_price": request.user.cart.items.all().aggregate(
                        Sum("price")
                    )["price__sum"]
                    or 0,
                }
            )
        total_price = (
            request.user.cart.items.all().aggregate(Sum("price"))["price__sum"] or 0
        )

        print(request.user.cart.items.all())

        return render(
            request,
            "cart/cart.html",
            {
                "total_price": total_price,
                "title": "Your Cart",
                "cart": "no",
            },
        )


class UpdateCart(LoginRequiredMixin, View):
    def post(self, request):
        data = json.loads(request.body)
        for item in data:
            try:
                # 2nd items is dict method
                for k, v in item.items():
                    ci = models.CartItem.objects.get(id=k)
                    ci.quantity = int(v)
                    ci.save()
            except Exception as e:
                pass

        cart = request.user.cart.items.values("id", "quantity", "price")
        total_price = request.user.cart.items.all().aggregate(Sum("price"))[
            "price__sum"
        ]
        return JsonResponse({"cart": list(cart), "total_price": total_price})
