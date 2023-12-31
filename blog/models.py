from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255,blank=True,null=True)
    profile_url = models.URLField(blank=True,null=True)
    def __str__(self):
        return self.name