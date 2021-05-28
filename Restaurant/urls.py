"""Restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"", include("Myrestaurant.urls", namespace="Myrestaurant")),]
#     # 会从这个接口获取到 图片信息。关于admin界面添加图片 是django admin自己添加的图片。
#     #               图片的路径         后面是你使用的配置文件  这些都是给serve函数用的。
#     path(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
