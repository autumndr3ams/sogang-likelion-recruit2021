from django.db import models

class Apply(models.Model):
    applyname = models.CharField(max_length=10,verbose_name='지원자명')
    phone = models.CharField(max_length=20, verbose_name='핸드폰번호')
