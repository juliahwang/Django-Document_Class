from django.http import HttpResponse, Http404
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
    # question_id가 pk인 Question 객체를 가져와
    try:
        question = Question.objects.get(pk=question_id)
    # production 상황에서는 절대로 DoesNotExist가 뜨면 안된다. 히스토리나 코드가 유출될 수 있기 때문.
    except Question.DoesNotExist as e:
        raise Http404('Question does not exist')

        # context라는 이름을 가진 dict에 'question'이라는 키값으로 위 변수를 할당
    context = {
        'question': question,
    }
    # 이후 'polls/detail.html'과 context를 렌더링한 결과를 리턴
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
