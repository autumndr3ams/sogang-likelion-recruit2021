from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import uuid
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

def set_profile_img_path(instance,filename):
    name = filename.split('.')[0]
    extension = filename.split('.')[-1]
    
    return f'profile_img/{instance.act_no}기_{instance.name}.{extension}'

class MyUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, email, password, **kwargs):
        """
        일반 유저 생성
        """
        kwargs.setdefault('is_admin', False)
        return self._create_user(email, password, **kwargs)
    def create_superuser(self, email, password, **kwargs):
        """
        관리자 유저 생성
        """
        kwargs.setdefault('is_admin', True)
        kwargs.setdefault('act_no',8)
        return self._create_user(email, password, **kwargs)

    def get_or_create_google_user(self,user_pk):
        user = MyUser.objects.get(pk=user_pk)
        user.save()
        return user
    
    def create_dummy_user(self,email,password,**kwargs):
        if not email:
            raise ValueError('이메일은 필수입니다.')

        # addr = email.split('@')[-1]
        # if addr != 'likelion.org':
        #     msg = '유효한 멋쟁이 사자처럼 이메일이 아닙니다.'
        #     raise ValueError(msg)

        user = self.model(email=self.normalize_email(email), **kwargs)

        # hash함수로 비밀번호 설정
        user.set_password(make_password(password))
        user.save(using=self._db)

class MyUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        get_latest_by = 'date_joined'

    uuid = models.UUIDField(
        primary_key=True, 
        unique=True,
        editable=False, 
        default=uuid.uuid4, 
        verbose_name='PK'
    )
    TEAM_CHOICES = (
        ('회장단','회장단'),
        ('홍보팀','홍보팀'),
        ('기획팀','기획팀'),
        ('교육팀','교육팀'),
    )
    POSITION_CHOICES = (
        ('회장','회장'),
        ('부회장','부회장'),
        ('팀장','팀장'),
        ('팀원','팀원'),
    )
    email = models.EmailField(unique=True, verbose_name='이메일')
    name = models.CharField(max_length=20,verbose_name = '이름')
    phone = models.CharField(max_length=11, verbose_name='핸드폰번호') # - 없이 핸드폰번호를 입력해주세요 placeholder로 쓰기
    act_no = models.IntegerField(blank=True,null=True,verbose_name='활동기수')
    
    is_manager = models.BooleanField(default=False, verbose_name='운영진 여부')
    profile_img = models.ImageField(
        blank=True,
        upload_to=set_profile_img_path,
        verbose_name='프로필이미지')
    team = models.CharField(max_length=20, choices = TEAM_CHOICES, verbose_name='팀')
    position = models.CharField(max_length = 20,choices = POSITION_CHOICES, verbose_name='직책')
    first_major = models.CharField(max_length=20,verbose_name='주전공')
    second_major = models.CharField(blank=True,max_length=20,verbose_name='부전공/연계전공')
    
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
    is_admin = models.BooleanField(default=False, verbose_name='관리자 여부')   

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        #"Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin