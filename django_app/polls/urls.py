from django.conf.urls import url
from . import views

# from polls import views 와 같은 뜻이다.
# 다만 같은 디렉터리 안에 있기 때문에 .으로 쓴다.

# namespace를 사용하여 앱마다 같은 이름을 가진 url을 구분
app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
