from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# signals.py is used to create Profile for User automatically
# when a User is saved then send signal(post_save) and signal will be received by decorator @receiver
# @receiver is our create_profile function which takes those 4 arguments passed from @receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # if user is created then create Profile with instance of created User


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
