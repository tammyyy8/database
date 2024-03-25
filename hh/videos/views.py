from django.http import JsonResponse
from .models import Video
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from django.core.exceptions import MultipleObjectsReturned

# Specific videos
def video_detail_api(request, username, slug):
    user = User.objects.get(username=username)
    try:
        video = Video.objects.get(user=user, slug=slug)
    except Video.DoesNotExist:
        raise Http404("Video does not exist")
    except MultipleObjectsReturned:
        video = Video.objects.filter(user=user, slug=slug).first()

    thumbnail_url = video.thumbnail.url if video.thumbnail else None
    if thumbnail_url:
        thumbnail_url = request.build_absolute_uri(thumbnail_url)
        
    data = {
        'title': video.title,
        'youtube_video_id': video.youtube_video_id,
        'thumbnail': thumbnail_url,
    }
    return JsonResponse(data)




# List of filtered videos
def video_list_api(request, username):
    videos = Video.objects.filter(user__username=username).order_by('order')

    video_data = []
    for video in videos:
        thumbnail_url = video.thumbnail.url if video.thumbnail else None
        if thumbnail_url:
            thumbnail_url = request.build_absolute_uri(thumbnail_url)

        video_data.append({
            'title': video.title,
            'youtube_video_id': video.youtube_video_id,
            'thumbnail': thumbnail_url,
            'order': video.order,
            'slug': video.slug
        })
        
    return JsonResponse({'videos': video_data})



