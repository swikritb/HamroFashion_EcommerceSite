# Generated by Django 3.0.7 on 2020-08-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_auto_20200812_1245"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
