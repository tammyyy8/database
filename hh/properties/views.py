# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import Property, PropertyImage, Profile
from django.db.models import F
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import PropertySerializer

# def properties_api(request):
#     properties = Property.objects.annotate(
#         order_priority=F('priority')
#     ).order_by('order_priority', '-price').values()

#     return JsonResponse(list(properties), safe=False)

def properties_api(request, username):
    built_in = request.GET.get('built_in', None)  # Extract built_in from query params
    
    if username:
        properties = Property.objects.filter(users__username=username)
    elif built_in:
        properties = Property.objects.filter(built_in=True)
    else:
        properties = Property.objects.all()
        
    properties = properties.annotate(
        order_priority=F('priority')
    ).order_by('order_priority', '-price').values()
    
    return JsonResponse(list(properties), safe=False)





def property_detail_api(request, username, slug):
    property_instance = get_object_or_404(Property, slug=slug, users__username=username)
    # Query images associated with the property
    images = PropertyImage.objects.filter(property=property_instance)
    image_urls = [image.image.url for image in images]


    # Get user's profile data
    profile_data = None
    try:
        profile = Profile.objects.get(user__username=username)
        profile_data = {
            "full_name": profile.full_name,
            "job_title": profile.job_title,
            "is_team": profile.is_team,
            "bio_short": profile.bio_short,
            # ... include all other fields that you want
        }
    except Profile.DoesNotExist:
        pass  # Handle the case where the profile doesn't exist

    property_data = {
        # "user_ids": list(property_instance.users.values_list('id', flat=True)),
        "name": property_instance.name,
        "built_in": property_instance.built_in,
        "slug": property_instance.slug, # Include the slug
        "address": property_instance.address,
        "unit_number": property_instance.unit_number,
        "city": property_instance.city,
        "state": property_instance.state,
        "postal_code": property_instance.postal_code,
        "price": str(property_instance.price), # Convert Decimal to string
        "description": property_instance.description,
        "tag": property_instance.tag,
        "bedrooms": property_instance.bedrooms,
        "bathrooms": str(property_instance.bathrooms), # Convert Decimal to string
        "year_built": property_instance.year_built,
        "interior_sqft": property_instance.interior_sqft,
        "lot_size": property_instance.lot_size,
        "youtube_video_id": property_instance.youtube_video_id,
        "images": image_urls, # Include image URLs
        "priority": property_instance.priority,
        "agent_data": profile_data
    }

    return JsonResponse(property_data)




def featured_properties_api(request, username):
    properties = Property.objects.filter(users__username=username, is_featured=True)
    
    # Apply the same sorting logic as in properties_api
    properties = properties.annotate(
        order_priority=F('priority')
    ).order_by('order_priority', '-price')
    
    property_list = []
    
    for property_instance in properties:
        images = PropertyImage.objects.filter(property=property_instance)
        image_urls = [image.image.url for image in images]

        property_data = {
            # "user_ids": list(property_instance.users.values_list('id', flat=True)),
            "name": property_instance.name,
            "built_in": property_instance.built_in,
            "slug": property_instance.slug,
            "address": property_instance.address,
            "unit_number": property_instance.unit_number,
            "city": property_instance.city,
            "state": property_instance.state,
            "postal_code": property_instance.postal_code,
            "price": str(property_instance.price),
            "description": property_instance.description,
            "tag": property_instance.tag,
            "bedrooms": property_instance.bedrooms,
            "bathrooms": str(property_instance.bathrooms),
            "year_built": property_instance.year_built,
            "interior_sqft": property_instance.interior_sqft,
            "lot_size": property_instance.lot_size,
            "youtube_video_id": property_instance.youtube_video_id,
            "images": image_urls,
            "priority": property_instance.priority,
        }
        property_list.append(property_data)

    response_data = {
        'count': len(property_list),
        'properties': property_list
    }
    
    return JsonResponse(response_data, safe=False)
