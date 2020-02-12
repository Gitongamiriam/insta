from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True,upload_to='images/')
    bio = models.TextField(blank=True)
    followers= models.ManyToManyField(User,related_name='followers', blank=True)
    following= models.ManyToManyField(User,related_name='following', blank=True)
  
    def __str__(self):
        return f"{self.user}'s Profile"


    
    @classmethod
    def search_user(cls, profile):
        profile = profile.objects.get(name=profile)
        profiles = cls.objects.filter(profile=profile.id)
        return profile

class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=30,blank=True)
    likes=models.ManyToManyField(User,blank = True,related_name = 'post_likes')
    post_time=models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User,on_delete = models.CASCADE)


    def __str__(self):
        return self.image_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def show_images(cls):
        post =cls.objects.order_by('post_time') 
        return post
           

 

   

