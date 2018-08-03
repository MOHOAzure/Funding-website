from django.conf.urls import url

from . import views

app_name = 'funding'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<team_id>[0-9]+)/fund/$', views.fund, name='fund'),
]