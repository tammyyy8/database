from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import os

def validate_file_size(value):
    filesize = value.size
    if filesize > 52428800:  # 50MB
        raise ValidationError(_("The maximum file size that can be uploaded is 50MB"))
    else:
        return value

# These are for setting the path for video/image uploads
def user_directory_path_video(instance, filename):
    return f'members/{instance.user.username}/videos/{filename}'
def user_directory_path_image(instance, filename):
    return f'members/{instance.user.username}/images/{filename}'

# Built-in videos
class BuiltInVideo(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='built_in_videos/', validators=[validate_file_size])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Username")
    # Custom fields
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Full Name")
    job_title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Job Title")
    is_team = models.BooleanField(default=False, verbose_name="Do you have a team or organization?")
    bio_short = models.TextField(blank=True, null=True, verbose_name="Short Biography (3-5 Sentences)")
    bio = models.TextField(blank=True, null=True, verbose_name="Full Biography")
    headline = models.CharField(max_length=255, blank=True, null=True, verbose_name="Homepage Headline")
    background_video = models.FileField(upload_to=user_directory_path_video, null=True, blank=True, validators=[validate_file_size], verbose_name="Homepage Background Video (Optional)")
    built_in_video = models.ForeignKey(BuiltInVideo, null=True, blank=True, on_delete=models.SET_NULL)
    background_image = models.ImageField(upload_to=user_directory_path_image, null=True, blank=True, verbose_name="Homepage Background Image (Optional)")
    home_page_lifestyle_image = models.ImageField(upload_to=user_directory_path_image, null=True, blank=True, verbose_name="Homepage Headshot / Lifestyle Image (1080X1080)")
    cta_headline = models.CharField(max_length=255, blank=True, null=True, verbose_name="CTA Headline")
    cta_body = models.TextField(blank=True, null=True, verbose_name="CTA Body Text")
    cta_button = models.CharField(max_length=255, blank=True, null=True, verbose_name="CTA Button Text")
    cta_image = models.ImageField(upload_to=user_directory_path_image, null=True, blank=True, verbose_name="CTA Background Image")
    phone = models.CharField(max_length=17, blank=True, null=True, verbose_name="Phone (Must be 12223334444 format)")
    email = models.EmailField(blank=True, null=True, verbose_name="Email Address")
    street = models.CharField(max_length=255, blank=True, null=True, verbose_name="Office Address #1")
    suite = models.CharField(max_length=100, blank=True, null=True, verbose_name="Office Address #2")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Office City")
    state = models.CharField(max_length=50, blank=True, null=True, verbose_name="Office State")
    postal_code = models.CharField(max_length=10, blank=True, null=True, verbose_name="Office Postal Code")
    custom_disclaimer = models.TextField(blank=True, null=True, verbose_name="Footer Disclaimer Text")
    youtube = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    headshot = models.ImageField(upload_to=user_directory_path_image, blank=True, null=True, verbose_name="Headshot Image (800X1000)")
    home_banner = models.ImageField(upload_to=user_directory_path_image, null=True, blank=True)
    properties_banner = models.ImageField(upload_to=user_directory_path_image, null=True, blank=True, verbose_name="Properties Banner")
    about_banner = models.ImageField(upload_to=user_directory_path_image, null=True, blank=True, verbose_name="About Banner")
    testimonials_banner = models.ImageField(upload_to=user_directory_path_image, null=True, blank=True, verbose_name="Testimonials Banner")
    videos_banner = models.ImageField(upload_to=user_directory_path_image, null=True, blank=True, verbose_name="Videos Banner")
    articles_banner = models.ImageField(upload_to=user_directory_path_image, null=True, blank=True, verbose_name="Articles Banner")
    favicon = models.ImageField(upload_to=user_directory_path_image, null=True, blank=True, verbose_name="Favicon")
    logo = models.ImageField(upload_to=user_directory_path_image, null=True, blank=True, verbose_name="Logo")
    legal_entity = models.CharField(max_length=255, blank=True, null=True, verbose_name="Legal Entity")

    def save(self, *args, **kwargs):
        try:
            this = Profile.objects.get(id=self.id)
            if this.background_video != self.background_video:
                this.background_video.delete(save=False)
            if this.background_image != self.background_image:
                this.background_image.delete(save=False)
        except: pass  # when new photo then we do nothing, normal case
        super(Profile, self).save(*args, **kwargs)

@receiver(models.signals.post_delete, sender=Profile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Profile` object is deleted.
    """
    if instance.background_video:
        if os.path.isfile(instance.background_video.path):
            os.remove(instance.background_video.path)
    if instance.background_image:
        if os.path.isfile(instance.background_image.path):
            os.remove(instance.background_image.path)