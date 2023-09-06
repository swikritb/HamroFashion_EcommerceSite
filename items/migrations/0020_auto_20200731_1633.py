# Generated by Django 3.0.7 on 2020-07-31 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0019_subcategory_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="photo",
            field=models.ImageField(
                default=None, upload_to="category/dp", verbose_name="Display Picture"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="items.Category",
            ),
        ),
    ]
