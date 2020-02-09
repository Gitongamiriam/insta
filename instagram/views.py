from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image

# Create your views here.
def home(request):
    posts=Image.show_images() 
  
    return render(request,'home.html',{'posts':posts})

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Image.search_by_profile('search_term')
        message = f"{search_term}"

        return render(request, 'search_results.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any profile"
        return render(request, 'search_results.html',{"message":message})    
