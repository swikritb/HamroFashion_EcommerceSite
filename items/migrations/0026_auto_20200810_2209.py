# Generated by Django 3.0.7 on 2020-08-10 22:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0025_item_code"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="instock",
        ),
        migrations.AddField(
            model_name="item",
            name="discount",
            field=models.FloatField(
                default=0,
                verbose_name="Write didcount percentage as decimal points like 0.1 for 10%, 0.35 for 35%, etc",
            ),
        ),
        migrations.AddField(
            model_name="item",
            name="status",
            field=models.CharField(
                choices=[("instock", "instock"), ("out of stock", "out of stock")],
                default="instock",
                max_length=12,
            ),
        ),
    ]
