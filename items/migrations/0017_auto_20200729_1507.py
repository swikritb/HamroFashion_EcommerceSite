# Generated by Django 3.0.7 on 2020-07-29 09:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0016_auto_20200729_1441"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="item",
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
        migrations.DeleteModel(
            name="CartItem",
        ),
    ]
