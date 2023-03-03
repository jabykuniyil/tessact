import datetime

from django.db import models
from user.models import UserProfile

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=32, null=False)
    blog_content = models.CharField(max_length=1028, null=True)
    media_url = models.CharField(max_length=1028, null=True)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(null=False, default=datetime.datetime.now())

    @property
    def get_author(self):
        return self
