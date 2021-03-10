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
        score = request.GET.get('score')
        result = {
            '0' : ['뜨거운 논쟁을 즐기는 서강이','당신은 본투비(born-to-be) 프론트엔드 능력자입니다!\n멋사에 지원하여 프론트엔드 개발자로서 세상을 바꾸어보지 않을래요?'],
            '1' : ['만능 재주꾼 서강이','당신은 백을 이해하는 프론트엔드 개발자로서 자질이 보이네요!\n백엔드를 이해하는 프론트엔드 개발자는 천하무적이죠!\n9기 아기사자로서, 세상을 바꿀 아이디어를 함께 만들어봐요!'],
            '2' : ['대담한 서강이','당신은 백엔드 기술에 대한 이해도가 높은 프론트엔드 개발자입니다!\n대담하게 세상을 바꿀 아이디어를 구현할 자질이 보이는데, 9기 아기사자가 되어보지 않겠어요?'],
            '3' : ['알바트로스','세상에! 그 귀하다는 풀스택 개발자로서의 자질이 보이시네요!\n태평양을 비행하는 알바트로스처럼 풀스택 개발자로서의 커리어, 그리고 세상을 바꿔보기 위해 9기 아기사자가 되어보지 않겠어요?'],
            '4' : ['자유로운 영혼의 알로스','당신은 디자인 감각이 넘치는 백엔드 개발자이시군요?\n미적 감각이 넘치는 자유로운 영혼의 알로스처럼 9기 아기사자로서 자유롭게 세상을 바꿀 아이디어를 만들어보아요!'],
            '5' : ['열정적인 활동가 알로스','당신은 매사에 열정적인 백엔드 개발자로서의 자질이 보이네요!\n미적 감각이 없지는 않지만, 프론트엔드 개발자는 적성에 안맞는 당신!\n9기 아기사자가 되어서, 팀원들과 세상을 바꿀 아이디어를 만들어보아요!'],
            '6' : ['엄격한 관리자 알로스','당신은 누구보다 엄격하고, 치밀한 백엔드 개발자로서의 자질이 보입니다!\n9기 아기사자가 되어서, 세상을 바꿀 샤프한 아이디어를 만들어보면 어떨까요?'],
        }

        context = {
            'score': score,
            'sogang_friends' : result[score][0],
            'sogang_story' : result[score][1],
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

#면접 시간 조정 페이지 뷰
# class InterviewHomeView(View) :
#     def get(self, request) :
#         return render(request, 'recruit/interview-home.html')

class InterviewSelectView(View) :
    def get(self, request) :
        name = request.GET['name']
        return render(request, 'recruit/interview-select.html',{'name' : name})

class InterviewResultView(View) :
    def get(self, request) :
        time = get_object_or_404(Content,pk=index)
        return render(request, 'recruit/interview-result.html',{'name' : name})