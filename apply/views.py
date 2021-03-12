from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth import update_session_auth_hash
from .models import Apply
from .forms import ApplyForm

class ApplyHomeView(View):
    form_class = ApplyForm
    template_name = 'recruit/interview-home.html'
    def get(self, request):
        return render(request,'recruit/interview-home.html')
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return redirect('recruit/interviewselect')
        return render(request,self.template_name,{'form':form})

