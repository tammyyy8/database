from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from members.models import Profile

class Property(models.Model):
    users = models.ManyToManyField(User, related_name='properties')
    name = models.CharField(max_length=200, verbose_name="Property Brand")
    built_in = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False, verbose_name="Add to Home Page?")
    address = models.CharField(max_length=200)  # Street Address
    unit_number = models.CharField(max_length=50, blank=True, null=True)  # Unit #
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Property Description")
    tag = models.CharField(max_length=50, blank=True, null=True, verbose_name="Property Tag")  # Renamed from status
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    year_built = models.PositiveIntegerField()
    interior_sqft = models.PositiveIntegerField()
    lot_size = models.PositiveIntegerField()
    youtube_video_id = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="Url Slug")
    priority = models.PositiveIntegerField(blank=True, null=True, default=None, verbose_name="Property Order")
    properties = models.ManyToManyField('self', through='PropertyOrder', symmetrical=False, related_name='related_properties')

    
    def save(self, *args, **kwargs):
        original_slug = slugify(self.name)
        unique_slug = original_slug
        num = 1
        while Property.objects.filter(slug=unique_slug).exclude(id=self.id).exists():
            unique_slug = f'{original_slug}-{num}'
            num += 1
        self.slug = unique_slug
        super(Property, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

def property_image_directory_path(instance, filename):
    return f'properties/{instance.property.slug}/images/{filename}'

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=property_image_directory_path)


class PropertyOrder(models.Model):
    property = models.ForeignKey(Property, related_name='ordered_properties', on_delete=models.CASCADE)
    related_property = models.ForeignKey(Property, related_name='orders', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']