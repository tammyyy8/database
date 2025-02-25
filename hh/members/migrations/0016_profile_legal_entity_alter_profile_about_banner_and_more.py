# Generated by Django 4.2.4 on 2023-12-07 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import members.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("members", "0015_profile_favicon_profile_logo"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="legal_entity",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Legal Entity"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="about_banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
                verbose_name="About Banner",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="articles_banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
                verbose_name="Articles Banner",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="background_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
                verbose_name="Homepage Background Image (Optional)",
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
                verbose_name="Homepage Background Video (Optional)",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.TextField(
                blank=True, null=True, verbose_name="Full Biography"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="bio_short",
            field=models.TextField(
                blank=True, null=True, verbose_name="Short Biography (3-5 Sentences)"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="city",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Office City"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="cta_body",
            field=models.TextField(blank=True, null=True, verbose_name="CTA Body Text"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="cta_button",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="CTA Button Text"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="cta_headline",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="CTA Headline"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="cta_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
                verbose_name="CTA Background Image",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="custom_disclaimer",
            field=models.TextField(
                blank=True, null=True, verbose_name="Footer Disclaimer Text"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="Email Address"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="favicon",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
                verbose_name="Favicon",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="full_name",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Full Name"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="headline",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Homepage Headline"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="headshot",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
                verbose_name="Headshot Image (800X1000)",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="home_page_lifestyle_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
                verbose_name="Homepage Headshot / Lifestyle Image (1080X1080)",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="is_team",
            field=models.BooleanField(
                default=False, verbose_name="Do you have a team or organization?"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="job_title",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Job Title"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="logo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
                verbose_name="Logo",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.CharField(
                blank=True,
                max_length=17,
                null=True,
                verbose_name="Phone (Must be 12223334444 format)",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="postal_code",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="Office Postal Code"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="properties_banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
                verbose_name="Properties Banner",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="state",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Office State"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="street",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Office Address #1"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="suite",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Office Address #2"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="testimonials_banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
                verbose_name="Testimonials Banner",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Username",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="videos_banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=members.models.user_directory_path_image,
                verbose_name="Videos Banner",
            ),
        ),
    ]
