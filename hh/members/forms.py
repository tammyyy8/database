from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'full_name', 'bio_short', 'bio', 'cta_headline', 'cta_body', 'phone',
            'email', 'street', 'suite', 'city', 'state', 'postal_code',
            'custom_disclaimer', 'youtube', 'facebook', 'instagram', 'twitter',
            'website', 'tiktok', 'linkedin', 'headshot'
        ]
