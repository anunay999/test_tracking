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
        return HttpResponseRedirect("/track")


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
    # iterating over the rows and
    # getting value from each cell in row
        for i in sheet.iterrows():#worksheet.iter_rows():#sheet.iterrows():
            row = pd.Series(i[1])
            #row_data = list()
            #for cell in row:
            #    row_data.append(str(cell.value))
            
            '''case = row_data[0]
            case_id = row_data[1]
            excel_data.append(row_data)
            '''
            
            case = row['Scenario'] #row_data[0]
            case_id = row['Kainos Automated TC ID']#row_data[1]
            name = request.POST['name']
            module = request.POST['module']
            email = request.POST['email']
            session = request.session.session_key
            obj = Tracker(name=name, email=email, module=module,
                kainos_id=case_id, scenario=case,session_id=session)
            obj.save()
            #remove_dups()
    except(NameError):
        return render(request, 'test_cases/error.html', {'error': 'Could not load the sheet'})
    # return render(request, 'test_cases/track.html', {"excel_data":excel_data})

    
def track(request):
    try:
        if("GET" == request.method):
            obj = Tracker.objects.filter(session_id=request.session.session_key)
            #choices = Tracker._meta.get_field('result').choices
            choices = ['Select','Pass','Fail']
            return render(request, 'test_cases/track.html', {'sheet': obj,'choices':choices})
        elif("POST"==request.method):
            obj = Tracker.objects.filter(session_id=request.session.session_key)
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
            return render(request, 'test_cases/error.html', {'error': l})

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
def browse(request):
    records  = Tracker.objects.all()
    mod = set()
    for i in records:
        mod.add(i.module)
    return render(request, 'test_cases/browse.html', {'module': mod})

def error(request):
    return render(request, 'test_cases/error.html', {})


def remove_dups():
    for row in Tracker.objects.all():
        if(Tracker.objects.filter(kainos_id=row.kainos_id).count() > 1):
            row.delete()
def module(request):
    if(request.method=="POST"):
        return redirect("track/")



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
