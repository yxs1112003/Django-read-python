from blog import views

from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.blog_index, name='blog_index'),
    # url(r'(?P<album_id>[0-9]+)^$', views.albumIndex, name='albumIndex'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/starts/$', views.vote, name='starts'),
]
