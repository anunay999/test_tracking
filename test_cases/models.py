import datetime
from django.db import models
from django.utils import timezone
from django import forms

class Tracker(models.Model):
    
    def __str__(self):
        return self.test_case+'Tested by '+self.tester+', Last Modifield on '+str(self.last_modified)+', Result '+str(self.result)
    scenario = models.CharField(max_length = 1000,null=True)
    kainos_id = models.CharField(max_length = 200,null=True)
    last_modified = models.DateTimeField('Last Modified',null=True)
    result = models.BooleanField(default=False,null=True)

class UploadFileForm(forms.form):
    file = forms.FileField(lavel='Upload Excel Sheet')
    
class LoginForm(forms.form,models.model):
     name = forms.CharField(label='Name',max_length=100)
     email = forms.CharField(label='Email',max_length=100)
     Module = forms.CharField(label='Module',max_length=100)
     track = models.ForeignKey(Tracker)
     
# Create your models here.
