from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import datetime

# Create your models here.
class role(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    #employees = look at user model
    def __str__(self):
        return self.name
    
class User(AbstractUser):
    role = models.ForeignKey(role, on_delete=models.CASCADE, null=True, blank=True, related_name="employees")
    #leadsassigned
    #useractivities
    #usertasks
    def __str__(self):
        return self.username
    
    
class lead(models.Model):
    fullname = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    number = models.CharField(max_length=12)
    timecreated = models.DateTimeField(auto_now_add=True)
    assignedto = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="leadsassigned")
    interest = models.CharField(max_length=25, blank=True, null=True)
    status = models.CharField(max_length=25,  blank=True, null=True)
    #leadactivity 
    #leadtasks
    def __str__(self):
        return self.fullname
    
class activity(models.Model):
    activitytype = models.CharField(max_length=25)
    text = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    oflead = models.ForeignKey(lead, on_delete=models.CASCADE, related_name="leadactivity")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="useractivities", blank=True, null=True)

class task(models.Model):
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    text = models.CharField(max_length=200)
    oflead = models.ForeignKey(lead, on_delete=models.CASCADE, related_name="leadtasks", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usertasks", blank=True, null=True)