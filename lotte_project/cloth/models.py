from django.db import models
from mypage.models import CustomUser
# Create your models here.

class StandardFit_up (models.Model) :
    # 반팔 긴팔
    clothType = models.CharField(max_length=10)
    # S M L XL
    size = models.CharField(max_length=5)
    # 가슴 둘레
    chest = models.IntegerField()
    # 어깨 넓이
    shoulder = models.IntegerField()
    # 팔 길이, 반팔일 때는 null
    sleeve = models.IntegerField(blank=True, null=True)
    # 옷의 총장
    clothGeneral = models.IntegerField()
    
class StandardFit_down(models.Model) :
    # 반바지 긴바지
    clothType = models.CharField(max_length=10)
    # S M L XL
    size = models.CharField(max_length=5)
    # 허리
    waistWidth = models.IntegerField()
    # 총 길이
    totalHeight = models.IntegerField()

class UpCloth (models.Model) :
    name = models.CharField(max_length=20, unique=True)
    clothImage = models.ImageField()
    multyFitType = models.ManyToManyField(StandardFit_up)

class DownCloth(models.Model) :
    name = models.CharField(max_length=20, unique=True)
    clothImage = models.ImageField()
    multyFitType = models.ManyToManyField(StandardFit_down)
