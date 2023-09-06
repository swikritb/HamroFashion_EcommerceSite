from django.urls import path
from . import views


urlpatterns = [
    path("", views.CheckOutView.as_view(), name="checkout"),
    path("order/<slug:url_code>/", views.DetailViewOrder.as_view(), name="order"),
]
