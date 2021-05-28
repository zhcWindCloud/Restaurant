from django.db import models
import random
from django.contrib.auth.models import User


# Create your models here.


# 用户表 菜单表 爱好表

class MenuType(models.Model):
    MenuType = models.CharField(max_length=10, verbose_name="分类")
    CreateType = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", editable=False)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name
        ordering = ['CreateType']

    def __str__(self):
        return self.MenuType


class MenuModels(models.Model):
    core = str(round(random.uniform(1, 5), 1))
    shell = str(random.randint(300, 700))
    free = str(round(random.uniform(5, 15), 1))
    MenuName = models.CharField(max_length=30, verbose_name="菜名")
    MenuType = models.ForeignKey(MenuType, related_name="Menutype", on_delete=models.CASCADE, verbose_name="类型")
    MenuImg = models.ImageField(upload_to='static/img/plants/', default='static/img/plants/default.png', max_length=200,
                                blank=True, null=True, verbose_name='图片')
    MenuCore = models.CharField(max_length=20, verbose_name="评分", blank=True, null=True, default=core)
    MenuShell = models.CharField(max_length=20, verbose_name="月销售量", blank=True, null=True, default=shell)
    MenuFree = models.CharField(max_length=20, verbose_name="价格", blank=True, null=True, default=free)
    CreateMenu = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", editable=False)

    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = verbose_name
        ordering = ['CreateMenu']

    def __str__(self):
        return self.MenuName


class LovableModels(models.Model):
    LoveUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="所属用户", related_name="lovableuser")
    LoveMune = models.ForeignKey(MenuModels, on_delete=models.CASCADE, verbose_name="所喜欢类型", related_name="loveMune")
    CreateMenu = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", editable=False)

    class Meta:
        verbose_name = "喜好"
        verbose_name_plural = verbose_name
        ordering = ['CreateMenu']

    def __str__(self):
        return self.LoveUser.username


class History(models.Model):
    History_User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户", related_name="histor_name")
    OrderMune = models.ForeignKey(MenuModels, on_delete=models.CASCADE, verbose_name="订单", related_name="order")
    CreateMenu = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", editable=False)

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name
        ordering = ['CreateMenu']

    def __str__(self):
        return self.History_User.username