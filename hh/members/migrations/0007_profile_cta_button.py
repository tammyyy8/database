# Generated by Django 4.2.4 on 2023-08-30 13:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0006_profile_is_team"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="cta_button",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
