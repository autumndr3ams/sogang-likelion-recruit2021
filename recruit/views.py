from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView
import json

from .models import BFQuestionnaire, BFTest

class HomeView(View):
    def get(self, request):
        return render(request,'recruit/home.html')

class BFTestView(ListView):
    model = BFQuestionnaire                 # queryset(default) = BFQuestionnaire.objects.all()
    template_name = 'recruit/bftest.html'
    context_object_name = 'q'               # rename template context var

    def get_queryset(self):
        return BFQuestionnaire.objects.get(pk=1)
    
    def post(self,request):
        q_pk = request.POST.get('q-pk')
        choice = request.POST.get('choice')
        q = get_object_or_404(BFQuestionnaire,pk=int(q_pk)+1)

        context = {
            'pk': q.pk,
            'front':q.front_ans,
            'back':q.back_ans,
            'question':q.question,
        }
        return HttpResponse(json.dumps(context),content_type="application/json")

    # context 확장시 overriding할 함수
    def get_context_data(self,**kwargs):
        context = super(BFTestView, self).get_context_data(**kwargs)
        return context

class BFResultView(TemplateView):
    template_name = 'recruit/bfresult.html'

    def get(self, request, *args, **kwargs):
        result = {
        '0' : '뜨거운 논쟁을 즐기는 서강이',
        '1' : '만능 재주꾼 서강이',
        '2' : '대담한 서강이',
        '3' : '알바트로스',
        '4' : '자유로운 영혼의 알로스',
        '5' : '열정적인 활동가 알로스',
        '6' : '엄격한 관리자 알로스'
        }

        score = request.GET.get('score')
        context = {
            'score': score,
            'sogang_friends' : result[score],
            'img_src': 'result_'+score+'.png',
        }
        return self.render_to_response(context)

# 히스토리 페이지 뷰
class HistoryView(View):
    def get(self, request):
        return render(request,'recruit/history.html')

# 서강사자 페이지 뷰
class SglionInfoView(View):
    def get(self, request):
        return render(request,'recruit/sglioninfo.html')