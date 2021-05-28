from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
# Register your models here.

admin.site.site_header = '菜单管理后台'
admin.site.site_title = '菜单管理后台'


@admin.register(MenuType)
class MenuType(admin.ModelAdmin):
    list_display=["MenuType"]
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10

@admin.register(MenuModels)
class MenuModels(admin.ModelAdmin):
        def upload_img(self, obj):
            try:
                img = mark_safe('<img src="/%s" width="50px" />' % (obj.MenuImg,))
                print(obj.MenuImg)
            except Exception as e:
                img = ''
                print(e)
            return img

        upload_img.short_description = "图片"
        upload_img.allow_tags = True
        list_display=["MenuName","MenuType","MenuCore","MenuShell","MenuFree","upload_img"]
        # list_per_page设置每页显示多少条记录，默认是100条
        list_per_page = 10

    # ordering设置默认排序字段，负号表示降序排序
    # ordering = ('-created_time',)

    # list_editable 设置默认可编辑字段，在列表里就可以编辑
    # list_editable = ['MenuName']

    # fk_fields 设置显示外键字段
        fk_fields = ['MenuType']

    #用于对指定字段的值进行搜索，支持模糊查询。列表类型，表示在这些字段上进行搜索。
    # search_fields = ['title']


# @admin.register(LovableModels)
# class LovableModels(admin.ModelAdmin):
#     def type(self,obj):
#         try:
#             Type = obj.LoveMune.MenuType.MenuType
#         except Exception as e:
#             Type = ''
#         return Type
#
#     type.short_description = "所属类型"
#     type.allow_tags = True
#
#     list_display = ["LoveUser", "type", "CreateMenu"]
#     # list_per_page设置每页显示多少条记录，默认是100条
#     list_per_page = 10
#

@admin.register(History)
class HistoryModels(admin.ModelAdmin):

    list_display = ["History_User", "OrderMune", "CreateMenu"]
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 10
