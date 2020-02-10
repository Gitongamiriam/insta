from django import forms
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()
class imagePostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude =[
            'likes',
            'post_time',
            'posted_by',
        ]