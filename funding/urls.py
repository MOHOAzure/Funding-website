from django.urls import path

from . import views

app_name = 'funding'

urlpatterns = [	
    path('', views.TeamList.as_view(), name='index'),    
    path('fund/', views.fund, name='fund'),
]
