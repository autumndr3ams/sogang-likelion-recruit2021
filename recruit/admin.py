from django.contrib import admin
from .models import BFQuestionnaire, BFTest

# Register your models here.
class BFQuestionnaireAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Statement', {'fields':['question']}),
        ('Answer Statement',{'fields':['front_ans','back_ans']})
    ]
admin.site.register(BFTest)
admin.site.register(BFQuestionnaire,BFQuestionnaireAdmin)
