from django.contrib import admin
# from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser
# for excel
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin


class MyAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['email','name']


admin.site.register(MyUser,MyAdmin)
# admin.site.unregister(Group)