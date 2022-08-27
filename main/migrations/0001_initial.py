# Generated by Django 4.1 on 2022-08-27 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Queue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("path", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=250)),
                ("created", models.DateTimeField()),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]