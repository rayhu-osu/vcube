from django.conf.urls import url

from . import views

app_name = 'demo'
urlpatterns = [
    # ex: /demo/
    url(r'^$', views.index, name='index'),
    # ex: /demo/5/
    url(r'^(?P<number_id1>[0-9]+)/$', views.detail, name='detail'),
    # ex: /demo/5/results/
    url(r'^(?P<number_id2>[0-9]+)/results/$', views.results, name='results'),
    # ex: /demo/5/vote/
    url(r'^(?P<number_id>[0-9]+)/vote/$', views.vote, name='vote'),
]