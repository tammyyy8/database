from django.contrib import admin
from django.contrib.auth.models import User
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            try:
                form.base_fields['user'].queryset = User.objects.filter(id=request.user.id)
                form.base_fields['user'].initial = [request.user.id]
            except Exception as e:
                print(f"Error: {e}")
        return form

admin.site.register(Video, VideoAdmin)