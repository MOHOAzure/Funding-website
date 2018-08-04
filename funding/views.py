from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Team

class TeamList(generic.ListView):
    template_name = 'funding/index.html'
    queryset = Team.objects.order_by('project')
    context_object_name = 'team_list'

class DetailView(generic.DetailView):
    model = Team
    template_name = 'funding/detail.html'
    
def fund(request):
    if request.is_ajax():
        team_id = request.POST.get('team_id')
        fund_to_be_add = request.POST.get('fund')
        team = Team.objects.get(pk=team_id)
        team.funds += int(fund_to_be_add)
        team.save()
        return HttpResponse('OK')    
    else:
        return HttpResponse('BAD')
      
