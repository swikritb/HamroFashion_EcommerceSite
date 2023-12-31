# Generated by Django 3.1 on 2020-08-17 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0033_auto_20200811_1619"),
    ]

    operations = [
        migrations.CreateModel(
            name="SLideImaages",
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
                (
                    "photo",
                    models.ImageField(upload_to="", verbose_name="put a slide image "),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="items.subcategory",
            ),
        ),
    ]
