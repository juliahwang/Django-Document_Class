from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question


def index(request):
    """
    최근 5개 질문에 대해 보여주는 뷰
    :param request: 요청
    :return: 최근 5개의 질문
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
