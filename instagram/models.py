from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='profiles/')
    bio=models.CharField(max_length=30,blank=True)
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.bio   

    @classmethod
    def search_profile(cls, profile):
        profile = profile.objects.get(name=profile)
        profiles = cls.objects.filter(profile=profile.id)
        return profile

    @classmethod
    def get_profile_by_id(cls, id):
        try:
            profile = cls.objects.get(id=id)
            print("Object found")
            return profile
        except DoesNotExist:
            print("object not found")       


    
  

class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=30,blank=True)
    likes=models.ManyToManyField(User,blank = True,related_name = 'post_likes')
    post_time=models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User,on_delete = models.CASCADE,blank=True)


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
           

 

   

