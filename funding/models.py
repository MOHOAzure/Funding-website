from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    project = models.CharField(max_length=50)
    funds = models.PositiveSmallIntegerField(default=0)    
    def __str__(self):
        return self.project
    
class DBSEMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gold = models.PositiveSmallIntegerField(default=10)
    def __str__(self):
        return self.user.username