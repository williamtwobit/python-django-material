from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='root'),
    url(r'^topics/(?P<topic_pk>\d+)/lessons/(?P<lesson_pk>\d+)/$', views.lesson, name='lesson'),
    url(r'^topics/(?P<pk>\d+)/$', views.topic, name='topic'),
]