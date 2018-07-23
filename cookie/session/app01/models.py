from django.db import models

# Create your models here.
class Userinfo(models.Model):
    user = models.CharField(max_length=12)
    pwd = models.CharField(max_length=12)