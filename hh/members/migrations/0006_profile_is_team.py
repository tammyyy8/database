# Generated by Django 4.2.4 on 2023-08-30 12:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0005_profile_headline"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="is_team",
            field=models.BooleanField(default=False),
        ),
    ]
