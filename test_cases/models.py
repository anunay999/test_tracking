import datetime
from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.sessions.models import Session



class Tracker(models.Model):
    choices =( 
    ("Pass","Pass"),("Fail","Fail")
    ) 
    name = models.CharField('Name',max_length=100,null=True)
    email = models.CharField('Email',max_length=100,null=True)
    module = models.CharField('Module',max_length=100,null=True)
    scenario = models.CharField('Scenario',max_length = 1000,null=True)
    kainos_id = models.CharField("Kainos Automated TC ID",max_length = 200,null=True)
    last_modified = models.DateTimeField('Last Modified',null=True)
    result = models.CharField('Result',choices = choices,max_length=10,null=True)
    session_id = models.ForeignKey(Session,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.scenario)+' ->  Tested by   '+str(self.name)

    
   # details = models.ForeignKey(LoginForm,on_delete=models.CASCADE)


# Create your models here.
