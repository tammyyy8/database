# Generated by Django 4.2.4 on 2023-12-07 22:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("testimonials", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testimonial",
            name="testimonial_body",
            field=models.TextField(verbose_name="Testimonial Body"),
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="testimonial_first_name",
            field=models.CharField(max_length=100, verbose_name="First Name"),
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="testimonial_last_name",
            field=models.CharField(max_length=100, verbose_name="Last Name"),
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="testimonial_title",
            field=models.CharField(max_length=200, verbose_name="Testimonial Title"),
        ),
    ]
