# Generated by Django 4.2.4 on 2023-08-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="homepage_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="homepage_images/"
            ),
        ),
    ]
