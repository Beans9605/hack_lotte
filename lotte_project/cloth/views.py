from django.shortcuts import render, get_object_or_404
from .models import Cloth
# Create your views here.

def clothHome(request) :
    cloths = Cloth.objects.all()

    context = {'cloths' : cloths}

    return render(request, "cloth/clothHome.html", context)


def selectCloth(request) :

    if request.method == 'POST' and request.user :
        name = request.POST['name']
        fitId = request.POST['fitId']
        cloth = Cloth.objects.filter(name=name, multyFitType=fitId).distinct()
        context = {'cloth' : cloth }
        return render(request, "", context)
    else :
        return render(request, "")

def shoppingPage (request) :
    if request.method == 'POST' :
        cloths = request.POST['cloths']
        