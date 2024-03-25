# Generated by Django 4.2.4 on 2023-09-04 13:40

from django.db import migrations, models
import members.models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0011_builtinvideo_alter_profile_background_video_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="homepage_image",
        ),
        migrations.AddField(
            model_name="profile",
            name="about_banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="articles_banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="home_banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="properties_banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="testimonials_banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="videos_banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="background_video",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_video,
                validators=[members.models.validate_file_size],
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="headshot",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
            ),
        ),
    ]
