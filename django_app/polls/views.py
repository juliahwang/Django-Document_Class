from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from polls.models import Question, Choice


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


### get_list_or_404() 사용하여 index() 만들기
# def index(request):
#     question = get_list_or_404(Question.objects.order_by('-pub_date')[:5])
#     context = {
#         'question': question,
#     }
#     return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # # production 상황에서는 절대로 DoesNotExist가 뜨면 안된다. 히스토리나 코드가 유출될 수 있기 때문.
    # except Question.DoesNotExist as e:
    #     raise Http404('Question does not exist')

    ### 다음 두 줄은 같은 의미이다(관계형데이터베이스 개념)
    # question.choice_set.all()
    # Choice.objects.filter(question=question).all()

    # question_id가 pk인 Question 객체를 가져와
    question = get_object_or_404(Question, pk=question_id)
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
    # request의 method가 POST방식일 때
    q = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        data = request.POST
        try:
            choice_id = data['choice']
            # 아래의 HttpResponse에 적절히 돌려준다.
            # return HttpResponse("You voted for {}.".format(choice_id))

            choice = Choice.objects.get(id=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('polls:results', question_id)
            # polls:results에서 results는 view도 가능.
        except (KeyError, Choice.DoesNotExist):
            # message프레임워크
            # request에 메세지를 저장해놓고 request에 대한 response를 돌려줄 때 메세지를 담아 보낸다.
            messages.add_message(
                request,
                messages.ERROR,
                "You didn't select a choice"
            )
            return redirect('polls:detail', question_id)
    else:
        return HttpResponse("You're voting for %s" % question_id)
