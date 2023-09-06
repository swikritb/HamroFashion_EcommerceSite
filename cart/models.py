from django.db import models
from django.contrib.auth.models import User
from items.models import Item
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.PositiveSmallIntegerField(null=False, blank=False)
    price = models.PositiveSmallIntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    belongs_to_order = models.BooleanField(default=False)

    def __str__(self):
        return "{} x {} ".format(self.item, self.quantity)

    def to_json(self):
        inner_resp = {}
        inner_resp["pic"] = self.item.pictures.first().image.url
        inner_resp["name"] = self.item.name
        inner_resp["quantity"] = self.quantity
        inner_resp["price"] = self.price
        inner_resp["detail"] = self.detail or "-"
        inner_resp["url"] = self.item.get_absolute_url()
        return inner_resp


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(CartItem)

    def __str__(self):
        if self.user:
            return f"{self.user}'s cart"
        else:
            return "Someone's cart"
