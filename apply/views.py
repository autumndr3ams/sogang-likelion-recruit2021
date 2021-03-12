from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth import update_session_auth_hash
from .models import Apply
from .forms import ApplyForm

class ApplyView(View):
    form_class = ApplyForm
    # initial = {'key':'value'}
    template_name = 'recruit/intervew-home.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})
    def post(self, request):
        form = self.form_class(request.POSTe)
        if form.is_valid():
            return redirect('recruit/interview-select')
        return render(request,self.template_name, {'form':form})
