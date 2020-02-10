from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Profile
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


@login_required(login_url='/accounts/login/')
def home(request):
    posts=Image.show_images() 
  
    return render(request,'home.html',{'posts':posts})

def search_results(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search_results.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_results.html',{"message":message})   

@login_required() 
def add_new_image_post(request):
    user = User.objects.get(id = request.user.id)
    if request.method == 'POST':
        form = imagePostForm(request.POST,request.FILES)
        if form.is_valid():
            newpost = form.save(commit = False)
            newpost.posted_by = user
            newpost.save()
            return redirect('/')
        else:
            messages.info(request,"all fields are required")
            return redirect('newpost')
    else:
        form = imagePostForm()
        return render(request,'new_post.html',{"form":form})
