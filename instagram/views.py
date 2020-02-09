from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Profile,Image

# Create your views here.
def home(request):
    image=Image.objects.all()  
    profile=Profile.objects.all()
    return render(request,'home.html',{'image':image,'profile':profile})

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_profile(search_term)
        message = f"{search_term}"

        return render(request, 'base.html/search_results.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'base.tml/search_results.html',{"message":message,"profile":profile})    
