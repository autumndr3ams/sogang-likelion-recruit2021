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
# from django.contrib.auth.hashers import check_password
# from django.contrib.auth.forms import PasswordChangeForm
# from django.views.generic import View
# from .helper import send_mail, email_auth_num
# from django.template.loader import render_to_string

# class SocialregisterView(View):
#     model = BFQuestionnaire
#     template_name = 'accounts/.html'

#     def socialregister(request):
#         profile = request.user
#         if request.method=='POST':
#             form=SocialAccountUpdateForm(request.POST,instance=profile)
#             if form.is_valid():
#                 form.save()
#             return redirect('set_address')
#         else:
#             form=SocialAccountUpdateForm(instance=profile)
#         return render(request,'registration/socialregister.html',{'form':form})