from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth import get_user_model
from django.views import View
from django.views.generic import TemplateView, ListView
# from django.contrib.auth import login
# from django.core.mail import EmailMessage
# from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .models import MyUser, MyUserManager
from .forms import SocialAccountSignUpForm
# from django.contrib.auth.hashers import check_password
# from django.contrib.auth.forms import PasswordChangeForm
# from django.views.generic import View
# from .helper import send_mail, email_auth_num
# from django.template.loader import render_to_string

class SocialregisterView(View):
    form_class = SocialAccountSignUpForm
    # initial = {'key':'value'}
    template_name = 'registration/socialregister.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})
    def post(self, request):
        profile = request.user
        form = self.form_class(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request,self.template_name, {'form':form})

class SglionInfoView(ListView):
    queryset = MyUser.objects.filter(is_manager=True).order_by("-team", "position")
    context_object_name = 'manager_list'
    template_name = 'recruit/sglioninfo.html'