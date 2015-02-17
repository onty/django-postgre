from django.shortcuts import render
from django.http import HttpResponse, Http404
from polls.models import Question
from django.template import RequestContext, loader

def index(request):
	latest_list = Question.objects.order_by('-pub_date')[:5]
	print latest_list
	template = loader.get_template('polls/index.html')
	return render(request, 'polls/index.html',{'latest_question_list':latest_list})
# Create your views here.

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404
    return render(request, 'polls/detail.html',{'question':question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
