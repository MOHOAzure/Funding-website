from django.conf.urls import url

from . import views

app_name = 'funding'

urlpatterns = [
    url(r'^$', views.TeamList.as_view(), name='index'),    
    url(r'^fund/$', views.fund, name='fund'),
]
