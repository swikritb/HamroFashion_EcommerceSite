# Generated by Django 4.2.4 on 2023-09-06 15:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0043_remove_item_realtimeprice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="description",
            field=ckeditor.fields.RichTextField(db_column="desp"),
        ),
        migrations.CreateModel(
            name="WebsiteSection",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("section_title", models.CharField(max_length=20, unique=True)),
                ("section_description", ckeditor.fields.RichTextField()),
                ("items", models.ManyToManyField(to="items.item")),
            ],
        ),
    ]