from django.db import models
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    profile_photo=models.profileField(upload_to='profiles/')
    bio=models.CharField(max_length=30,blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.bio        

class profile(models.Model):
    profile=models.profileField(upload_to='profiles/')
    profile_name=models.CharField(max_length=30)
    profile_caption=models.CharField(max_length=30,blank=True)
    profile=models.ForeignKey(Profile)
    likes=models.IntegerField()
    comments=models.CharField(max_length=30,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.profile_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_id(cls, id):
        try:
            profile = cls.objects.get(id=id)
            print("Object found")
            return profile
        except DoesNotExist:
            print("object not found")    

    @classmethod
    def search_profiles(cls, profile):
        profile = profile.objects.get(name=profile)
        profiles = cls.objects.filter(profile=profile.id)
        return profiles)    

