# Generated by Django 4.1.3 on 2022-11-10 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dish",
            options={"verbose_name_plural": "dishes"},
        ),
    ]
