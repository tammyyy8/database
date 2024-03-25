from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from .models import Testimonial
from members.models import Profile, User

def get_testimonials(request, username, page=1):
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    testimonials = Testimonial.objects.filter(user=user)
    
    # Pagination logic
    items_per_page = int(request.GET.get('itemsPerPage', 8))  # Now dynamic
    paginator = Paginator(testimonials, items_per_page)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    # Serialize the page's testimonials
    serialized_testimonials = list(page.object_list.values())

    return JsonResponse({
        'testimonials': serialized_testimonials,
        'total': paginator.count,
        'page': page.number,
        'total_pages': paginator.num_pages,
        'user': username,
    })

def get_all_testimonials(request, username):
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    testimonials = Testimonial.objects.filter(user=user)
    
    # Serialize all testimonials
    serialized_testimonials = list(testimonials.values())

    return JsonResponse({
        'testimonials': serialized_testimonials,
        'total': len(serialized_testimonials),
        'user': username,
    })