from django.urls import path
from .views import *
from . import Ajax
from django.contrib.auth import views as auth_views
app_name = "Myrestaurant"

urlpatterns = [
    path("login/",login,name='login'),
    path('mylogin/', Ajax.mylogin, name="mylogin"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name='user_logout'),  # 退出
    path("", index, name="index"),
    path(r"detail/<int:id>/", detail,name= "detail"),
    path(r"type/<int:id>/", item),
    path(r"all/", getall),
    path(r"search/",search),
    path(r"free/", free,name='free'),
    path(r"order/", order, name='ORDER'),
    path(r'myorder/', Ajax.myorder, name="myorder"),
    path("mune/",Ajax.mymune,name = "mymune")


]
