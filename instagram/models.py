from django.db import models


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

