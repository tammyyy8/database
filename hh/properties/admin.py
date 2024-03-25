from django.contrib import admin
from django import forms
from .models import *


# Inline for PropertyImage
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3

# Inline for PropertyOrder
class PropertyOrderInline(admin.TabularInline):
    model = PropertyOrder
    extra = 1
    fk_name = 'property'

class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'priority']
    list_editable = ['priority']
    inlines = [PropertyImageInline, PropertyOrderInline]
    
    def get_form(self, request, obj=None, **kwargs):
        kwargs['exclude'] = ['built_in']
        form = super().get_form(request, obj, **kwargs)
        
        # Directly modify the form here, without creating a new class
        if not request.user.is_superuser:
            try:
                form.base_fields['users'].queryset = User.objects.filter(id=request.user.id)
                form.base_fields['users'].initial = [request.user.id]
                form.base_fields['users'].widget = forms.CheckboxSelectMultiple()
            except Exception as e:
                print(f"Error: {e}")
        
        return form
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(users=request.user)

# Proxy model for Built-In Property
class BuiltInProperty(Property):
    class Meta:
        proxy = True
        verbose_name = 'Built-In Property'
        verbose_name_plural = 'Built-In Properties'

# Admin for Built-In Property
class BuiltInPropertyAdmin(PropertyAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(built_in=True)

# Unregister Property if it's already registered to avoid conflicts
try:
    admin.site.unregister(Property)
except admin.sites.NotRegistered:
    pass

# Register both Property and BuiltInProperty
admin.site.register(Property, PropertyAdmin)
admin.site.register(BuiltInProperty, BuiltInPropertyAdmin)


