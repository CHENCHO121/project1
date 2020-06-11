from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(max_length=500, blank=True)
    phone_no=models.CharField(max_length=12, blank=True)
    dob=models.DateField(null=True,blank=True)
    profile_img=models.ImageField(upload_to='User/', null=True, blank=True)


class Contact(models.Model):
    name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=50,blank=True)
    phone=models.CharField(max_length=12,blank=False)
    msg=models.CharField(max_length=600,blank=False)

    def __str__(self):
        return(self.name)



# @receiver(post_save,sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save,sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.Profile.save()
