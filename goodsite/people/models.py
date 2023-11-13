from django.db import models


# Create your models here.

class Students(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)
