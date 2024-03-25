# Generated by Django 4.2.4 on 2023-12-07 22:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0003_alter_article_article_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="article_body",
            field=ckeditor.fields.RichTextField(verbose_name="Artile Boldy"),
        ),
        migrations.AlterField(
            model_name="article",
            name="banner",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="members/images/",
                verbose_name="Artile Banner",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="learn_more_link",
            field=models.URLField(verbose_name="CTA Button"),
        ),
        migrations.AlterField(
            model_name="article",
            name="order",
            field=models.IntegerField(default=0, verbose_name="Order"),
        ),
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(unique=True, verbose_name="Url Slug"),
        ),
        migrations.AlterField(
            model_name="article",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="members/videos/",
                verbose_name="Artile Thumbnail",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=255, verbose_name="Artile Title"),
        ),
        migrations.AlterField(
            model_name="article",
            name="youtube_video_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="YouTube Video ID"
            ),
        ),
    ]
