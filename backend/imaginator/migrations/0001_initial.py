# Generated by Django 3.0.5 on 2020-06-24 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DeepColorResult",
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
                ("original", models.ImageField(upload_to="")),
                ("colored", models.ImageField(upload_to="")),
                ("strategy", models.CharField(max_length=20)),
            ],
        ),
    ]
