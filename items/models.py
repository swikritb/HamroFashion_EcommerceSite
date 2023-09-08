from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from collections import Counter
from ckeditor.fields import RichTextField

from django.template.defaultfilters import slugify

from PIL import Image

from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.


def validateRate(value):
    if value < 0.0 or value > 5.0:
        raise ValidationError("Rating cannot be greater than zero")


def validated_discount(value):
    if value > 0.8:
        raise ValidationError("Discount can only be up to 80% or 0.8")

class WebsiteSection(models.Model):
    section_title = models.CharField(max_length=40, unique=True, blank=False, null=False)
    section_description = RichTextField(blank=True, null=True)
    items = models.ManyToManyField("items.Item")

    class Meta:
        verbose_name_plural = "Website Sections"
        ordering = ["-id"]

    def __str__(self) -> str:
        return self.section_title
    

class Photo(models.Model):
    image = models.ImageField(
        upload_to="items/pp", max_length=200, null=False, blank=False
    )

    def __str__(self):
        return self.image.name

    def save(self):
        super().save()
        image = Image.open(self.image.path)
        image = image.resize((500, 500), Image.ADAPTIVE)
        image.save(self.image.path)


class Item(models.Model):
    name = models.CharField(max_length=20, unique=True, blank=False, null=False)
    price = models.IntegerField(verbose_name="Pricing in NRS", blank=False, null=False)
    description = RichTextField(blank=False, null=False, db_column="desp")
    date_added = models.DateField(auto_now=True, db_column="dateadded")
    pictures = models.ManyToManyField(Photo)
    code = models.SlugField(max_length=50, null=True, blank=True)
    discount = models.FloatField(
        validators=[validated_discount],
        verbose_name="Write did count percentage as decimal points like 0.1 for 10%, 0.35 for 35%, etc",
        default=0,
        blank=False,
        null=False,
    )

    status = (
        ("instock", "instock"),
        ("out of stock", "out of stock"),
    )

    status = models.CharField(
        choices=status, max_length=len("out of stock"), default="instock"
    )

    def is_available(self):
        if self.status == "instock":
            return True
        return False

    is_available.boolean = True

    @property
    def real_time_price(self):
        return int(self.price - (self.price * self.discount))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"code": self.code})

    def save(self, *args, **kwargs):
        self.code = slugify(self.name)
        return super().save()


class SlideImages(models.Model):
    photo = models.ImageField(verbose_name="put a slide image", upload_to="slide/pic")
    link = models.URLField(
        verbose_name="redirects to", max_length=1000, null=True, blank=True
    )

    def __str__(self):
        return "Image no " + str(self.id)
