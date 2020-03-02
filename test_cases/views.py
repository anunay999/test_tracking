from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import pandas as pd
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from .models import Tracker
from django.views.decorators.csrf import csrf_exempt, csrf_protect
#from .models import ModelWithFileField
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import MultipleObjectsReturned
import openpyxl
from django.shortcuts import redirect
import datetime
import pandas as pd
import uuid
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
import xlwt

def login(request):
    if(request.method=="GET"):
        return render(request,'test_cases/login.html',{})
    elif(request.method=="POST"):
        username = request.POST['name']
        password = request.POST['password']
        #request.session['name'] 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('/track/browse/')
        else:
            return render(request,'test_cases/login.html',{'message':'Invalid Username or Password'})


def base(request):
    if(request.method=="GET"):
        return HttpResponseRedirect('/login')


def logout(request):

    if(request.method=='GET'):
        auth_logout(request)
        return render(request,'test_cases/logout.html',{})
    


# Create your views here.
def index(request):
    try:
        if(request.method == "GET"):
            return render(request, 'test_cases/index.html', {})

        elif(request.method == 'POST'):
            load_workbook(request)
            return HttpResponseRedirect("/track")


    except(NameError, MultiValueDictKeyError, Tracker.DoesNotExist):
        return render(request, 'test_cases/error.html', {'error': 'Please check the information and try again@'})
    except(MultipleObjectsReturned):
        return render(request, 'test_cases/error.html', {'error': 'Multiple Objects Returned'})
    else:
        return redirect(reverse('/track/browse/'),permanent=True)


def load_workbook(request):
    try:
        excel_file = request.FILES["file"]

    # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)
        sheet = pd.read_excel(excel_file)

    # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        import_id = str(uuid.uuid1())
            
    # iterating over the rows and
    # getting value from each cell in row
        for i in sheet.iterrows():#worksheet.iter_rows():#sheet.iterrows():
            row = pd.Series(i[1])
            #row_data = list()
            #for cell in row:
            #    row_data.append(str(cell.value))
            
            '''
            case = row_data[0]
            case_id = row_data[1]
            excel_data.append(row_data)
            '''
            request.session['uuid'] = import_id
            request.session['name'] = request.POST['name']
            case = row['Scenario'] #row_data[0]
            case_id = row['Kainos_ID']#row_data[1]
            name = request.POST['name']
            module = request.POST['module']
            email = request.POST['email']
            
            obj = Tracker(name=name, email=email, module=module,
                kainos_id=case_id, scenario=case,uuid=import_id)
            obj.save()

            #remove_dups()
    except(NameError):
        return render(request, 'test_cases/error.html', {'error': 'Could not load the sheet'})
    # return render(request, 'test_cases/track.html', {"excel_data":excel_data})


@permission_required('test_cases.can_view', login_url='/login/')
def track(request):
    try:
        if("GET" == request.method):
            import_id = request.session['uuid']
            obj = Tracker.objects.filter(uuid=import_id)
            #choices = Tracker._meta.get_field('result').choices
            choices = ['Select','Pass','Fail']
            return render(request, 'test_cases/track.html', {'sheet': obj,'choices':choices})
        elif("POST"==request.method):
            import_id = request.session['uuid']
            obj = Tracker.objects.filter(uuid = import_id)
            kainos = 'kainos_id'
            res = 'result'
            records = len(obj)+1
            l = []
            for i in range(1,records):
                kainos_id = request.POST[kainos+str(i)]
                result = request.POST[res+str(i)]
                record = obj.get(kainos_id=kainos_id)
                record.result=result
                record.last_modified = timezone.now()
                record.save()
                l.append(record)
            return redirect('browse/')
                #record = obj.get(kainos_id=kainos_id)
                #record.result = result
                #record.last_modified = datetime.now()
                #record.save()
                #return render(request, 'test_cases/error.html', {'error': record})

    except(NameError):
            return render(request, 'test_cases/error.html', {'error': 'Could not load the sheet'})

    
    #elif("POST" == request.method):
        #return render(request, 'test_cases/error.html', {'error':"result"})

        #kainos_id = request.POST['kainos_id1']
        #results=Tracker._meta.get_field('result').choices
        
        #return render(request, 'test_cases/error.html', {'error': kainos_id})
        #obj = Tracker(kainos_id=kainos_id,result=result,last_modified=datetime.now)
        
        #obj.last_modified = datetime.now()
        #obj = Tracker.objects.all()
@permission_required('test_cases.can_view', login_url='/login/')
def browse(request):
    if(request.method=='GET'):
        records  = Tracker.objects.all()
        mod = set()
        for i in records:
            mod.add(i.module)
        return render(request, 'test_cases/browse.html', {'module': mod})


def error(request):
    return render(request, 'test_cases/error.html', {})


@permission_required('entity.can_view', login_url='/login/')
def edit(request,module):
    if(request.method=="GET"):
        records = Tracker.objects.filter(module = module)
        return render(request, 'test_cases/edit.html', {'records':records,"module":module})
    elif(request.method=="POST"):
        obj = Tracker.objects.filter(module=module)
        kainos = 'kainos_id'
        res = 'result'
        records = len(obj)+1
        l = []    
        for i in range(1,records):        
            kainos_id = request.POST[kainos+str(i)]
            result = request.POST[res+str(i)]
            record = obj.get(kainos_id=kainos_id)
            record.result=result
            record.last_modified = timezone.now()
            record.save()
            remove_dups()
            l.append(record)
        records  = Tracker.objects.all()
        mod = set()
        for i in records:
            mod.add(i.module)
        return render(request, 'test_cases/browse.html', {'module': mod}) #render(request,'test_cases/module.html',{'records':obj,'module':obj})
        

def remove_dups():
    for row in Tracker.objects.all():
        if(Tracker.objects.filter(kainos_id=row.kainos_id).count() > 1):
            row.delete()


@permission_required('test_cases.can_view', login_url='/login/')
def module(request,module):
    if(request.method=="GET"):
        records = Tracker.objects.filter(module=module)
        return render(request,'test_cases/module.html',{'records':records,'module':module})


def upload(request):
    try:
        if(request.method == "GET"):
            return render(request, 'test_cases/index.html', {})

        elif(request.method == 'POST'):
            load_workbook(request)
            render(request, 'upload.html', {'successful_submit': True})

    except(NameError, MultiValueDictKeyError, Tracker.DoesNotExist):
        return render(request, 'test_cases/error.html', {'error': 'Please check the information and try again@'})
    except(MultipleObjectsReturned):
        return render(request, 'test_cases/error.html', {'error': 'Multiple Objects Returned'})
    else:
        return HttpResponseRedirect("/track")

def dashboard(request):
    labels = []
    data = []
    records  = Tracker.objects.all()
    mod = set()
    for i in records:
        mod.add(i.module)
    labels = list(mod)
    for i in mod:
        data.append(Tracker.objects.filter(module=i).count())

    return render(request, 'dashboard.html', {
        'labels': labels,
        'data': data,
    })


'''def index(request):
    #session = get_object_or_404(Tracker)
    try:
        if request.method == "POST":
            def choice_func(row):
                q = Tracker.objects.filter(slug=row[0])[0]
                row[0] = q
                return row
            if form.is_valid():
                request.FILES['file'].save_book_to_database(
                models=[Tracker, LoginForm],
                initializers=[None, choice_func],
                mapdicts=[
                    {
                    "Scenario": "scenario",
                    "Kainos Automated TC ID": "kainos_id",
                    "Last Modified": "last_modified",
                    "Name": "name",
                    "Email": "email",
                    "Module":"Module"
                }]
            )
            return redirect('test_cases/track.html')
        else:
            return HttpResponseBadRequest()

    except(KeyError, Tracker.DoesNotExist,MultiValueDictKeyError):
        return render(request,'test_cases/index.html',{'error_message':'Please check the information and try again@'})

  
@csrf_exempt
def upload_file_view(request):
    return _upload_file_view(request)

@csrf_protect
def _upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = ModelWithFileField(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('/main/track/')
    else:
        form = UploadFileForm()
    return render(request, 'test_cases/index.html', {'case': form})
def track(request):
    if "GET" == request.method:
        return render(request, 'test_cases/track.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)
        sheet = pd.read_excel(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            #for cell in row:
            #    row_data.append(str(cell.value))
            data = row[0]
            excel_data.append(row_data)
        return render(request,'test_cases/error.html',{'error':sheet.iloc[0,'Kainos Automated TC ID']})
        #return render(request, 'test_cases/track.html', {"excel_data":excel_data})
    
'''
# return render(request, 'test_cases/track.html', {'case': 'Hello'})
