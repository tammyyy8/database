from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Artile Title")
    youtube_video_id = models.CharField(max_length=255, null=True, blank=True, verbose_name="YouTube Video ID")
    thumbnail = models.ImageField(upload_to='members/videos/', null=True, blank=True, verbose_name="Artile Thumbnail")
    banner = models.ImageField(upload_to='members/images/', null=True, blank=True, verbose_name="Artile Banner")
    slug = models.SlugField(unique=True, verbose_name="Url Slug")
    order = models.IntegerField(default=0, verbose_name="Order")
    created_at = models.DateTimeField(default=timezone.now)
    article_body = RichTextField(verbose_name="Artile Boldy")
    learn_more_link = models.URLField(verbose_name="CTA Button")

    def save(self, *args, **kwargs):
        # Implement deletion logic for thumbnail
        # ...
        super().save(*args, **kwargs)
