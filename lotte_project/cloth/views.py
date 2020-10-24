from django.shortcuts import render, get_object_or_404
from .models import Cloth, ViewOfUser
from django.dispatch import Signal

clothDone = Signal()

# 콜백함수
class CallbackCloth :

    def send_done(self, clothData, user) :
        clothDone.send(sender=self, clothData=clothData, user=user)
        
# Create your views here.


def clothHome(request) :
    cloths = Cloth.objects.all()
    if request.user :
        user_views = ViewOfUser.objects.filter(users=request.user)
        views = ViewOfUser.objects.all()
        context = {'cloths' : cloths, 'user_views' : user_views, 'views' : views}
    else :
        views = ViewOfUser.objects.all()
        context = {'cloths' : cloths, 'views' : views}
    
    CallbackCloth.send_done(clothHome, clothData=context, user=None)
    return render(request, "cloth/clothHome.html", context)


def selectCloth(self, request) :
    if request.method == 'POST' and request.user :
        name = request.POST['name']
        fitId = request.POST['fitId']
        cloth = Cloth.objects.filter(name=name, multyFitType=fitId).distinct()
        context = {'cloth' : cloth }
        # signal을 이용한 신호를 받아서 데이터 조회 이후에 조회수 및 정보 저장 별도
        CallbackCloth.send_done(selectCloth, clothData=cloth, user=request.user)
        return render(request, "", context)
    else :
        return render(request, "")

# def shoppingPage (self, request) :
#     if request.method == 'POST' :
#         cloths = request.POST['cloths']
            