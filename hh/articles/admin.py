from django.contrib import admin
from django import forms
from django.contrib.auth.models import User  # Don't forget to import User
from ckeditor.widgets import CKEditorWidget
from .models import Article

class ArticleAdminForm(forms.ModelForm):
    article_body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Article
        fields = '__all__'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    form = ArticleAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['user'].queryset = User.objects.filter(id=request.user.id)
        return form

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
