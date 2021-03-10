from django.contrib import admin
from .models import Apply
class ApplyAdmin(admin.ModelAdmin):
    list_display = ('applyname', 'phone')

admin.site.register(Apply,ApplyAdmin)