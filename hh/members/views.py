from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, ProfileRegisterForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileRegisterForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('some_view') # Redirect to the desired page
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileRegisterForm()
    return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form})


def get_member_info(request, username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        headshot_url = request.build_absolute_uri(profile.headshot.url) if profile.headshot else None
        homepage_image_url = request.build_absolute_uri(profile.home_banner.url) if profile.home_banner else None
        home_banner_url = request.build_absolute_uri(profile.home_banner.url) if profile.home_banner else None
        properties_banner_url = request.build_absolute_uri(profile.properties_banner.url) if profile.properties_banner else None
        about_banner_url = request.build_absolute_uri(profile.about_banner.url) if profile.about_banner else None
        testimonials_banner_url = request.build_absolute_uri(profile.testimonials_banner.url) if profile.testimonials_banner else None
        videos_banner_url = request.build_absolute_uri(profile.videos_banner.url) if profile.videos_banner else None
        articles_banner_url = request.build_absolute_uri(profile.articles_banner.url) if profile.articles_banner else None
        favicon_url = request.build_absolute_uri(profile.favicon.url) if profile.favicon else None
        logo_url = request.build_absolute_uri(profile.logo.url) if profile.logo else None
        data = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'full_name': profile.full_name,
            'job_title':profile.job_title,
            'is_team': profile.is_team,
            'bio_short': profile.bio_short,
            'bio': profile.bio,
            'background_video': request.build_absolute_uri(str(profile.background_video.url)) if profile.background_video else None,
            'built_in_video': request.build_absolute_uri(str(profile.built_in_video.video_file.url)) if profile.built_in_video else None,
            'background_image': request.build_absolute_uri(str(profile.background_image.url)) if profile.background_image else None,
            'headline': profile.headline,
            'home_page_lifestyle_image': request.build_absolute_uri(str(profile.home_page_lifestyle_image.url)) if profile.home_page_lifestyle_image else None,
            'cta_headline': profile.cta_headline,
            'cta_body': profile.cta_body,
            'cta_button': profile.cta_button,
            'cta_image': request.build_absolute_uri(str(profile.cta_image.url)) if profile.cta_image else None,
            'phone': profile.phone,
            'email': profile.email,
            'street': profile.street,
            'suite': profile.suite,
            'city': profile.city,
            'state': profile.state,
            'postal_code': profile.postal_code,
            'custom_disclaimer': profile.custom_disclaimer,
            'youtube': profile.youtube,
            'facebook': profile.facebook,
            'instagram': profile.instagram,
            'twitter': profile.twitter,
            'website': profile.website,
            'tiktok': profile.tiktok,
            'linkedin': profile.linkedin,
            'headshot': request.build_absolute_uri(str(profile.headshot.url)) if profile.headshot else None,
            'homepage_image': homepage_image_url,
            'home_banner': home_banner_url,
            'properties_banner': properties_banner_url,
            'about_banner': about_banner_url,
            'testimonials_banner': testimonials_banner_url,
            'videos_banner': videos_banner_url,
            'articles_banner': articles_banner_url,
            'favicon': favicon_url,
            'logo': logo_url

            

        }
        return JsonResponse(data)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
