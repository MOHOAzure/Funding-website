from django.contrib import admin

from .models import Team
from .models import Funder

admin.site.register(Team)
admin.site.register(Funder)
