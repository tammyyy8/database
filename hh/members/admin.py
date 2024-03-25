from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, BuiltInVideo

# Update your ProfileAdminForm
class ProfileAdminForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)
    custom_disclaimer = forms.CharField(widget=forms.Textarea, required=False)  # Add this line

    class Meta:
        model = Profile
        fields = '__all__'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ['user', 'full_name', 'phone', 'email']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['user'].queryset = User.objects.filter(id=request.user.id)
        return form

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_select_related = ('profile',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)
    

class BuiltInVideoAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(BuiltInVideo, BuiltInVideoAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
