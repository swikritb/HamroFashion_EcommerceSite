from django.db import models
from django.urls import reverse
from django.conf import settings
from uuid import uuid1
from base64 import urlsafe_b64encode

from cart import models as cart_models
from hashlib import sha1
import datetime

# Create your models here.

User = settings.AUTH_USER_MODEL


class CheckoutProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
    address = models.CharField(max_length=40, null=True, blank=False)
    email = models.EmailField(max_length=60, null=True, blank=False)
    phone_no = models.CharField(max_length=20, verbose_name="Your Phone number")
    message = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ["-created_date"]


# create order
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    items = models.ManyToManyField(cart_models.CartItem)
    created_date = models.DateField(auto_now=True, db_column="cdate")
    address = models.CharField(max_length=40, null=False, blank=False)
    phone_no = models.CharField(max_length=40, null=False, blank=False)
    discount_amount = models.IntegerField(
        null=True, blank=True, default=0, db_column="discountamount"
    )
    url_code = models.SlugField(
        max_length=100, null=True, blank=True, db_column="urlcode"
    )
    initial_price = models.IntegerField(
        null=True, blank=True, default=0, db_column="initialprice"
    )
    total_price = models.IntegerField(
        null=True, blank=True, default=0, db_column="totalprice"
    )
    email = models.EmailField(max_length=100, blank=True, null=True)
    uuid_code = models.CharField(
        max_length=22, blank=True, null=True, db_column="uuidcode"
    )

    def mail_confirmation(self):
        pass

    def get_absolute_url(self):
        return reverse("order", kwargs={"url_code": self.url_code})

    def __str__(self):
        return f"{self.user} on {self.created_date}"

    def save(self):
        self.uuid_code = urlsafe_b64encode(uuid1().bytes)[0:22].decode("utf-8")
        self.url_code = sha1(
            str(
                str(datetime.datetime.now()) + str(self.user.password) + str(self.user)
            ).encode()
        ).hexdigest()
        return super().save()
