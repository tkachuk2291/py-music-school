# Generated by Django 4.1 on 2024-04-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("musician", "0002_musician_date_of_applying"),
    ]

    operations = [
        migrations.AlterField(
            model_name="musician",
            name="date_of_applying",
            field=models.DateField(auto_now_add=True),
        ),
    ]
