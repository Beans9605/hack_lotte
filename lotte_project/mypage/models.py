from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser (AbstractUser) :
    face_img = models.ImageField() 
    weight = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    fit = models.CharField(max_length=10)
    faceLength = models.FloatField(default=22.9)

class Image(models.Model): #이미지 업로드 테스트용 
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title