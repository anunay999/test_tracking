def logout(request):

    if(request.method=='GET'):
        auth_logout(request)
        return render(request,'test_cases/logout.html',{})


def login(request):
    if(request.method=="GET"):
        '''if(request.user.is_authenticated()):
            return  HttpResponseRedirect('/track/browse/')
        '''
        return render(request,'test_cases/login.html',{})
    elif(request.method=="POST"):
        username = request.POST['name']
        password = request.POST['password']
        #request.session['name'] 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return HttpResponseRedirect('/track/browse/')
        else:
            return render(request,'test_cases/login.html',{'message':'Invalid Username or Password'})
    

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
            request.session['name'] = request.user.get_full_name()
            case = row['Scenario'] #row_data[0]
            case_id = row['Kainos_ID']#row_data[1]
            name = request.user.get_full_name()
            module = request.POST['module']
            email = request.user.email
            category = request.POST['category']
            
            obj = Tracker(name=name, email=email, module=module,
                kainos_id=case_id, scenario=case,uuid=import_id,category=category)
            obj.save()
            #remove_dups()
    except(NameError):
        return render(request, 'test_cases/error.html', {'error': 'Could not load the sheet'})
    # return render(request, 'test_cases/track.html', {"excel_data":excel_data})

