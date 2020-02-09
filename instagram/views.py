from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Profile,Image

# Create your views here.
def home(request):
    return render(request,'home.html')
