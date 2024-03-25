"""
URL configuration for hh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from properties.views import *
from members.views import *
from testimonials.views import *
from videos.views import *
from articles.views import *
from contactform.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/properties/<str:username>/all/', properties_api, name='properties_api'),
    path('api/properties/featured/<str:username>/', featured_properties_api, name='featured_properties_api'),
    path('api/properties/<str:username>/<slug:slug>/', property_detail_api, name='property_detail_api'),
    path('api/member/<str:username>/', get_member_info, name='get_member_info'),
    path('api/testimonials/<str:username>/', get_all_testimonials, name='get_all_testimonials'),
    path('api/testimonials/<str:username>/<int:page>/', get_testimonials, name='get_testimonials'),
    path('api/videos/<str:username>/', video_list_api, name='video_list_api'),
    path('api/videos/<str:username>/<str:slug>/', video_detail_api, name='video_detail_api'),
    path('api/articles/<str:username>/', article_list_api, name='article_list_api'),
    path('api/articles/<str:username>/<str:slug>/', article_detail_api, name='article_detail_api'),
    path('api/contactform/<str:username>/', contact_form_api, name='contactform_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
