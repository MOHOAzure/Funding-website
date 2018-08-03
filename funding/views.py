from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
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
    
def fund(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return HttpResponseRedirect(reverse('funding:index'))
