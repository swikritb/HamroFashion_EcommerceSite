# Generated by Django 4.2.4 on 2023-09-01 15:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0039_alter_item_addinfo_alter_item_category_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="subcategory",
        ),
    ]