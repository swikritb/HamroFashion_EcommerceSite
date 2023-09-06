from django.conf import settings
from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver
from . import models


@receiver(pre_save, sender=models.CartItem)
def cartItem(sender, instance=None, *args, **kwargs):
    instance.price = instance.item.real_time_price * instance.quantity


# If user is created lets make a cart for the user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_cart(sender, instance=None, created=False, **kwargs):
    if created:
        models.Cart(user=instance).save()
