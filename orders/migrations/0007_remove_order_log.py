# Generated by Django 4.2.4 on 2023-09-06 10:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Orders_for_checkout", "0006_auto_20200828_1608"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="log",
        ),
    ]
