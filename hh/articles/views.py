from django.http import JsonResponse, Http404
from .models import Article
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned

# Specific articles
def article_detail_api(request, username, slug):
    user = User.objects.get(username=username)
    try:
        article = Article.objects.get(user=user, slug=slug)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    except MultipleObjectsReturned:
        article = Article.objects.filter(user=user, slug=slug).first()

    thumbnail_url = article.thumbnail.url if article.thumbnail else None
    if thumbnail_url:
        thumbnail_url = request.build_absolute_uri(thumbnail_url)
        
    data = {
        'user': article.user.username,  # Assuming User model has a username field
        'title': article.title,
        'youtube_video_id': article.youtube_video_id,
        'thumbnail': thumbnail_url,
        'banner': request.build_absolute_uri(article.banner.url) if article.banner else None,
        'slug': article.slug,
        'order': article.order,
        'created_at': article.created_at,
        'article_body': article.article_body,
        'learn_more_link': article.learn_more_link
    }
    return JsonResponse(data)

# List of filtered articles
def article_list_api(request, username):
    articles = Article.objects.filter(user__username=username).order_by('order')

    article_data = []
    for article in articles:
        thumbnail_url = article.thumbnail.url if article.thumbnail else None
        if thumbnail_url:
            thumbnail_url = request.build_absolute_uri(thumbnail_url)

        article_data.append({
            'user': article.user.username,  # Assuming User model has a username field
            'title': article.title,
            'youtube_video_id': article.youtube_video_id,
            'thumbnail': thumbnail_url,
            'banner': request.build_absolute_uri(article.banner.url) if article.banner else None,
            'slug': article.slug,
            'order': article.order,
            'created_at': article.created_at,
            'article_body': article.article_body,
            'learn_more_link': article.learn_more_link
        })

        
    return JsonResponse({'articles': article_data})
