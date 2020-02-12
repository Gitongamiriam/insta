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
    posts=Image.objects.all() 
    profile = Profile.objects.filter(user = request.user)

  
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
        form = ImagePostForm(request.POST,request.FILES)
        if form.is_valid():
            newpost = form.save(commit = False)
            newpost.posted_by = request.user

            newpost.save()
        return redirect('home')

        # else:
        #     messages.info(request,"all fields are required")
        #     return redirect('newpost')
    else:
        form = ImagePostForm()
        return render(request,'new_post.html',{"form":form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            # p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()
        context = {
            'u_form': u_form,
            'p_form': p_form
    }
    return render(request, 'profile.html', context)

 
                                                         

