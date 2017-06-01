from django.db import models


# Create your models here.
class Question(models.Model):  # 테이블명은 polls_question이 된다.
    question_text = models.CharField('질문내용', max_length=200)  # 필드의 이름은 컬럼의 이름이 된다.
    pub_date = models.DateTimeField('발행일자')
    # Field클래스를 정의할 때 첫 옵션 인수를 사용하면 필드의 이름을 사용자정의할 수 있다.


class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name='해당 질문', on_delete=models.CASCADE)
    # ForeignKey의 경우 다른 필드 인스턴스와는 달리 이름변수를 verbose_name으로 주어야한다.
    # ForeignKey를 통해 각 Choice클래스마다 Question과 연결된다.
    choice_text = models.CharField('선택내용', max_length=200)
    votes = models.IntegerField('총 투표수', default=0)
