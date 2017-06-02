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
    # lateset_question_list라는 키로 위 쿼리셋을 전달
    # polls/index.html을 이용해 render한 결과를 리턴
    context = {
        'latest_question_list': latest_question_list,
    }
    # Template DoesNot Exist
    # settings.py에서 template 디렉토리 경로를 바꿔줘야한다
    # os.path.join()에서 TEMPLATE_DIR을 정해준다.
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
