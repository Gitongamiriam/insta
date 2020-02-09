from django.db import models



# Create your models here.
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='profiles/')
    bio=models.CharField(max_length=30,blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.bio        

class Image(models.Model):
    image=models.ImageField(upload_to='images/')
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=30,blank=True)
    profile=models.ForeignKey(Profile)
    likes=models.IntegerField()
    comments=models.CharField(max_length=30,blank=True)
    post_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def show_images(cls):
        return cls.objects.order_by('post_time')
           

    # @classmethod
    # def get_profile_by_id(cls, id):
    #     try:
    #         profile = cls.objects.get(id=id)
    #         print("Object found")
    #         return profile
    #     except DoesNotExist:
    #         print("object not found")    

    # @classmethod
    # def search_profiles(cls, profile):
    #     profile = profile.objects.get(name=profile)
    #     profiles = cls.objects.filter(profile=profile.id)
    #     return profiles

