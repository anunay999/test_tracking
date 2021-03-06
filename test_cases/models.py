import datetime



class Tracker(models.Model):
    choices =(("None","None"),("Pass","Pass"),("Fail","Fail"))
    name = models.CharField('Name',max_length=100,null=True)
    #email = models.CharField('Email',max_length=100,null=True)
    module = models.CharField('Module',max_length=100,null=True)
    category = models.CharField('Category',max_length=100,null=True)
    
    scenario = models.CharField('Scenario',max_length = 1000,null=True)
    case_id = models.CharField("ID",max_length = 200,null=True)
    last_modified = models.DateTimeField('Last Modified',null=True)
    result = models.CharField('Result',choices = choices,max_length=10,null=True)
    uuid = models.CharField('uuid',max_length = 1000,null=True) #models.ForeignKey(Session,on_delete=models.CASCADE)
    
    
    
    
    '''
    choices =(("Pass","Pass"),("Fail","Fail"))
    name = models.CharField('Name',max_length=100,null=True)
    email = models.CharField('Email',max_length=100,null=True)
    module = models.CharField('Module',max_length=100,null=True)
    category = models.CharField('Category',max_length=100,null=True)
    
    scenario = models.CharField('Scenario',max_length = 1000,null=True)
    kainos_id = models.CharField("Kainos Automated TC ID",max_length = 200,null=True)
    last_modified = models.DateTimeField('Last Modified',null=True)
    result = models.CharField('Result',choices = choices,max_length=10,null=True)
    uuid = models.CharField('uuid',max_length = 1000,null=True) #models.ForeignKey(Session,on_delete=models.CASCADE)
    '''
    def __str__(self):
        return ' Module : '+str(self.module)+' Category : '+str(self.category)+' ID:'+str(self.id)
    
    
   # details = models.ForeignKey(LoginForm,on_delete=models.CASCADE)


# Create your models here.
