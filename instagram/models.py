from django.db import models
import datetime as dt


# Create your models here.
class Profile(models.Model):
    profile_photo=models.CharField(max_length=30,blank=True)
    bio=models.CharField(max_length=30,blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        save.delete()

    def __str__(self):
        return self.profile_photo        

class Image(models.Model):
    image=models.CharField(max_length=30)
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=30,blank=True)
    profile=models.ForeignKey(Profile)
    likes=models.IntegerField()
    comments=models.CharField(max_length=30,blank=True)
    post_time=models.DateTimeField(auto_now_add=True)

