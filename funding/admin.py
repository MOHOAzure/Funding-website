from django.contrib import admin

from .models import Team
from .models import DBSEMember

admin.site.register(Team)
admin.site.register(DBSEMember)
