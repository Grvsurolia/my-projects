from django.db import models
from employees.models import User
# Create your models here.
from django.utils.translation import ugettext_lazy as _



class Team(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    team_image = models.ImageField(_("team_image"), upload_to='upload/', blank=True,null=True)
    date_time = models.DateTimeField(auto_now=True,blank=True,null=True)
    
    
    def __str__(self):
        return self.name



class Invitation(models.Model):
    ROLE_CHOICES = (

            ('owner', 'owner'),
            ('member', 'Member'),
    )
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='owner')
    is_accepted = models.BooleanField(default=False)
    invited_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='invited_by')
    date_time = models.DateTimeField(auto_now=True,blank=True,null=True)


    def __str__(self):
        return self.email
        

class Member(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    member = models.ManyToManyField(User)

    def __str__(self):
        return str(self.team)