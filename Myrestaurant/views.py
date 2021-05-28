
from django.shortcuts import render

from .models import *
import random


# Create your views here.


def login(request):
    return render(request, 'Login.html')


def index(request):
    lits = []
    cou = MenuModels.objects.all().count() - 1
    print(MenuType,type(MenuModels.objects.values))
    for i in range(5):
        img = MenuModels.objects.all()[random.randint(1, cou)]
        if img in lits:
            pass
        else:
            lits.append(img)
    pls = MenuType.objects.all()[:30]
    cats = MenuModels.objects.all()

    return render(request, 'index.html', locals())



def detail(request, id):
    try:
        p = MenuModels.objects.get(id=id)
        pls = MenuType.objects.all()
        res = MenuModels.objects.filter(MenuType=p.MenuType.id).exclude(id=id)[:6]
        object = User.objects.get(username=request.user)
        count = LovableModels.objects.filter(LoveUser=object).count() - 1
        object_list = []
        for x in range(count*2):
            l = LovableModels.objects.filter(LoveUser=object)[random.randint(0, count)]
            if l.LoveMune not in object_list :
                object_list.append(l.LoveMune)

    except:
        pass
    return render(request, 'detail.html', locals())




def item(request, id=None):
    cats = MenuModels.objects.filter(MenuType=id)
    pls = MenuType.objects.all()
    return render(request, 'plist.html', locals())


def getall(request):
    res = MenuModels.objects.all()
    cats = MenuType.objects.all()
    pls = MenuType.objects.all()
    return render(request, 'all.html', locals())


def search(request):
    res = MenuModels.objects.filter(MenuName__contains=request.GET.get('wd'))
    res1 = MenuModels.objects.filter(MenuType=MenuType.objects.filter(MenuType__contains=request.GET.get('wd')).first())
    cats = MenuType.objects.all()
    return render(request, 'res.html', locals())


def free(request):
    free = 'free'
    return render(request, "free.html", locals())


def order(request):
    free = 'order'
    try:
        object = User.objects.get(username=request.user)
        M_object = History.objects.filter(History_User=object)
        return render(request, "free.html", locals())
    except:
        return render(request, "free.html", locals())
