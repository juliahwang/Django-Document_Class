"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from polls import urls as polls_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^polls/', include('polls.urls')),
    # polls/패턴 뒤에 $를 붙이지 않을 때는 polls/urls.py으로 이동하여(include()) 패턴과 일치하는 url을 추가로 매치.
    url(r'^polls/', include(polls_urls)),
    # 두 방법 모두 기능한다.
    #url(r'^polls/', polls.urls)
    # 위와 같이는 기능하지 않는다(polls에 __init__.py가 없으므로.
]
