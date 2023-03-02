from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user_name = models.CharField(unique=True, max_length=16, null=False)
    email_id = models.EmailField(null=False)
    first_name = models.CharField(max_length=32, null=False)
    last_name = models.CharField(max_length=32, null=False)
    password = models.CharField(max_length=200, null=False)
    phone_number = models.CharField(max_length=10, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=256, null=True)




