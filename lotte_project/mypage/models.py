from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser (AbstractUser) :
    face_img = models.ImageField()
    weight = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    fit = models.CharField(max_length=10)
    faceLength = models.FloatField(default=22.9)