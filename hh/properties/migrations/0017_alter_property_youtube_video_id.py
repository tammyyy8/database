# Generated by Django 4.2.4 on 2023-09-04 23:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("properties", "0016_property_is_featured"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="youtube_video_id",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
