# Generated by Django 3.0.7 on 2020-08-03 16:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0005_cartitem_detail"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="price",
        ),
    ]
