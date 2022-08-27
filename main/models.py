from django.db import models

# Create your models here.
class Queue(models.Model):
    path = models.CharField(max_length=255)
    status = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
