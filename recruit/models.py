from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

class BFTest(AbstractBaseUser):
    BF_CHOICES = (
        ('back','backend'),
        ('front','frontend'),
    )
    participant = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='참여자'
    )
    choice = models.CharField(choices=BF_CHOICES,max_length=10,blank=False,verbose_name='테스트')
    result = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(6)],default=0,verbose_name='결과')

    class Meta:
        verbose_name = '심리테스트'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return f'[{self.pk}] - {self.result}'

class BFQuestionnaire(models.Model):
    question = models.CharField(max_length=30,blank=False,verbose_name='질문')
    front_ans = models.TextField(verbose_name='프론트엔드 답변')
    back_ans = models.TextField(verbose_name='백엔드 답변')

    class Meta:
        verbose_name = '질문지'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return f'{self.pk} - {self.question}'
