from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Video Title")
    youtube_video_id = models.CharField(max_length=255, verbose_name="YouTube Video ID")
    thumbnail = models.ImageField(upload_to='videos/thumbnails/', null=True, blank=True, verbose_name="Video Thumbnail")
    slug = models.SlugField(unique=True, verbose_name="Url Slug")
    order = models.IntegerField(default=0, verbose_name="Video Order")
    created_at = models.DateTimeField(default=timezone.now)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
