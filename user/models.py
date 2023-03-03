from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

# Create your models here.


class UserProfile(models.Model):
    user_name = models.CharField(max_length=16, null=False)
    email_id = models.EmailField(null=False)
    first_name = models.CharField(max_length=32, null=False)
    last_name = models.CharField(max_length=32, null=False)
    password = models.CharField(max_length=200, null=False)
    phone_number = models.CharField(max_length=10, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=256, null=True)
    notify_user = models.BooleanField(default=True, null=False)


@receiver(pre_save, sender=UserProfile)
def user_pre_save(sender, instance, *args, **kwargs):
    if instance.id and instance.notify_user:
        instance.notify_user = False


@receiver(post_save, sender=UserProfile)
def user_post_save(sender, instance, *args, **kwargs):
    if instance.id:
        instance.notify_user = False

