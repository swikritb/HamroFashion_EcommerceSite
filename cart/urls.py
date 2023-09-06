from django.urls import path, include
from . import views

urlpatterns = [
    path("addtocart/", views.AddToCart.as_view(), name="add_to_cart"),
    path("", views.ViewCart.as_view(), name="cart"),
    path("remove/", views.RemoveFromCart.as_view(), name="removefromcart"),
    path("clear/", views.ClearCart.as_view(), name="clearcart"),
    path("update/", views.UpdateCart.as_view(), name="updatecart"),
]
