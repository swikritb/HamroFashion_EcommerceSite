# Generated by Django 4.2.4 on 2023-09-06 12:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_remove_user_dob"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="s2nl",
        ),
    ]
