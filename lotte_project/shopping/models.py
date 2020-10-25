from django.db import models
from cloth.models import *

from mypage.models import CustomUser
# Create your models here.

class ShoppingBasket (models.Model) :
    multyUpCloths = models.ManyToManyField(UpCloth)
    multyDownCloths = models.ManyToManyField(DownCloth)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

