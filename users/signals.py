from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User) # sender is sending a post_save signal when user is saved and the signal will be recieved by the reciever
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User) # sender is sending a post_save signal when user is saved and the signal will be recieved by the reciever
def save_profile(sender,instance,**kwargs):
    instance.profile.save()



