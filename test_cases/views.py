from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
import pandas as pd
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from .models import Tracker,LoginForm,UploadFileForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
#from .models import ModelWithFileField
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def index(request):
    #session = get_object_or_404(Tracker)
    try:
        if request.method == "POST":
        form = LoginForm(request.POST)
        file = UploadFileForm(request.FILES)   
        excel_file = request.FILES[‘files’]

        def choice_func(row):
            q = Question.objects.filter(slug=row[0])[0]
            row[0] = q
            return row
        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[Question, Choice],
                initializers=[None, choice_func],
                mapdicts=[
                    {
                    "Question Text": "question_text",
                    "Publish Date": "pub_date",
                    "Unique Identifier": "slug"
                }]
            )
            return redirect('handson_view')
        else:
            return HttpResponseBadRequest()

    except(KeyError, Tracker.DoesNotExist,MultiValueDictKeyError):
        return render(request,'test_cases/index.html',{'error_message':'Please check the information and try again@'})

'''    
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
'''
def track(request):
    return render(request, 'test_cases/track.html', {'case': form})
    




        