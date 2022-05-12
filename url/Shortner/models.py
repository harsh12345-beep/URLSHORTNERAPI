from pyexpat import model
from re import T
from django.db import models

# Create your models here.

class UrlShortner(models.Model):
    Complete_Url = models.CharField(max_length=100)
    Shorten_Url = models.CharField(null=True,blank=True,max_length=30)
    def __str__(self):
        self.Complete_Url
