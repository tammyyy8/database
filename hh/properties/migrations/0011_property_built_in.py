# Generated by Django 4.2.4 on 2023-08-30 15:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "properties",
            "0010_property_city_property_postal_code_property_state_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="built_in",
            field=models.BooleanField(default=False),
        ),
    ]
