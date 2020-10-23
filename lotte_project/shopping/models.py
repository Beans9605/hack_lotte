from django.db import models
from cloth.models import *
from mypage.models import CustomUser
# Create your models here.

class ShoppingBasket (models.Model) :
    multyCloths = models.ManyToManyField(Cloth)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)