# Generated by Django 4.2.4 on 2023-08-30 20:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("properties", "0015_remove_featuredlistingorder_featured_listing_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
    ]
