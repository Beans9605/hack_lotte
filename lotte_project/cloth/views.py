from django.shortcuts import render, get_object_or_404
from .models import UpCloth, DownCloth
# Create your views here.

def clothHome(request) :
    upcloth = UpCloth.objects.all()
    downcloth = DownCloth.objects.all()

    context = {'upcloth' : upcloth, 'downcloth' : downcloth}

    return render(request, "", context)


def selectCloth(request) :
    if request.method == 'POST'  :
        name = request.POST['name']
        fitId = request.POST['fitId']
        if request.POST['clothType'] == 'up' :
            upcloth = UpCloth.objects.filter(name=name, multyFitType=fitId)
            return render(request, '', {'upcloth': upcloth})
        elif request.POST['clothType'] == 'down' :
            downcloth = DownCloth.objects.filter(name=name, multyFitType=fitId)
            return render(request, '', {'downcloth' : downcloth})
    else :
        return render(request, "")
    