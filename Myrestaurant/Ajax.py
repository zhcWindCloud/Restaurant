from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.contrib.auth import authenticate, login
from . import forms
import datetime
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

# pwd='4562154'
# mpwd=make_password(pwd,None,'pbkdf2_sha256')  # 创建django密码，第三个参数为加密算法
# pwd_bool=check_password(pwd,mpwd)# 返回的是一个bool类型的值，验证密码正确与否



# 登陆ajax验证
@csrf_exempt
@require_POST
def mylogin(request):
    login_form = forms.LoginForm(request.POST)
    username = request.POST.get("username")
    psd = request.POST.get("psd")
    re = HttpResponse()
    re.set_cookie('username','username')
    if login_form.is_valid():
        cd = login_form.cleaned_data
        user = authenticate(username=cd.get("username"), password=cd.get("psd"))
        if user:
            login(request, user)
            return HttpResponse("1")
        return HttpResponse("0")




@csrf_exempt
@require_POST
def mymune(request):
    user = request.POST.get("user",None)
    munename = request.POST.get("munename",None)
    print(user,munename)
    if user and munename:
        try:
            object = User.objects.get(username=user)
            M_object = models.MenuModels.objects.get(MenuName= munename)
            models.History.objects.create(History_User=object,OrderMune=M_object,CreateMenu=datetime.datetime.now())
            models.LovableModels.objects.create(LoveUser=object,LoveMune=M_object,CreateMenu=datetime.datetime.now())
            return HttpResponse("1")
        except:
            return HttpResponse("2")






@csrf_exempt
@require_POST
def myorder(request):
    ID = request.POST.get("ID",None)
    print(ID)
    if ID :
        try:
            M_OBJECT = models.History.objects.filter(id=ID).delete()
            return HttpResponse("1")
        except:
            return HttpResponse("2")
    return HttpResponse("3")


