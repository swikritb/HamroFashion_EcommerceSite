# Generated by Django 3.0.7 on 2020-08-11 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0032_reviewreply"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviewreply",
            name="review",
            field=models.ForeignKey(
                default="100",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="items.Review",
            ),
        ),
    ]