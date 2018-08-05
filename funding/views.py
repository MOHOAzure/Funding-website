from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Team

class TeamList(LoginRequiredMixin, generic.ListView):
    template_name = 'funding/index.html'
    queryset = Team.objects.order_by('project')
    context_object_name = 'team_list'
    
@login_required(login_url='/accounts/login/')
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
      
