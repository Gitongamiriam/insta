from django import forms
from django.contrib.auth import get_user_model
from . models import *

User = get_user_model()
class ImagePostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude =[
            'likes',
            'post_time',
            'posted_by',
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_pic"]        