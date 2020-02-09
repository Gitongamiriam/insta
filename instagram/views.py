from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Profile,Image

# Create your views here.
def home(request):
    images= Image.object.all()
    profiles=Profile.object.all()
    return render(request,'home.html',{'images':images,'profiles':profiles})
