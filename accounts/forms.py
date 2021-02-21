from django import forms
from .models import MyUser,MyUserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm ,SetPasswordForm,ReadOnlyPasswordHashField
from allauth.socialaccount.forms import SignupForm

# class ManagerForm(forms.ModelForm):
#     class Meta:
#         model = Manager
#         fields = ['name','email','phone','act_no']

# sociallogin form
class SocialAccountSignUpForm(forms.ModelForm):
    class Meta():
        model = MyUser
        fields = ['name', 'act_no','phone']
        