from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView
import json

from .models import BFQuestionnaire, BFTest

class HomeView(View):
    def get(self, request):
        return render(request,'recruit/base.html')

class BFTestView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'recruit/bftest.html')

class BFResultView(TemplateView):
    template_name = 'recruit/bfresult.html'

    def get(self, request, *args, **kwargs):
        score = request.GET.get('score')
        context = {
            'score': score,
        }
        return self.render_to_response(context)

def bftest(request):
    q = BFQuestionnaire.objects.get(pk=1)
    q_count = BFQuestionnaire.objects.count()

    if request.method == "POST":
        q_pk = request.POST.get('q-pk')
        q = get_object_or_404(BFQuestionnaire,pk=int(q_pk)+1)
        choice = request.POST.get('choice')
        
        context = {
            'pk': q.pk,
            'front':q.front_ans,
            'back':q.back_ans,
            'question':q.question,
        }
        return HttpResponse(json.dumps(context),content_type="application/json")

    return render(request,'recruit/bftest.html',{'q':q})
