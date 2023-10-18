from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.urls import reverse
import csv
import os
import json
from django.core.files.storage import FileSystemStorage
from employees.models import IdcUtilization
from employees.models import IDCVPHeadcountV
from employees.models import IDCDomainHeadcountV
from employees.models import IDCDomainHoursV
from employees.models import IDCVPHoursV
from employees.models import ATSVPVendorEmpV
from employees.models import ATSDEPTVendorEmpV
from django.core import serializers
from django.core.serializers import serialize


def dict_clean(items):
    result = {}
    for key, value in items:
        if value is None:
            value = ''
        result[key] = value
    return result

def employees(request):

    idcschedulefinish_datapoints = json.loads(serialize("json", IdcUtilization.objects.all()))
    idcschedulefinish_datapointsnew = []
    for row in idcschedulefinish_datapoints:
        dict_str = json.dumps(row["fields"])
        row["fields"] = json.loads(dict_str, object_pairs_hook=dict_clean)
        idcschedulefinish_datapointsnew.append(row["fields"])
    
    idcvphc_datapoints = json.loads(serialize("json", IDCVPHeadcountV.objects.all()))
    idcsvphc_datapointsnew = []
    for row in idcvphc_datapoints:
        dict_str = json.dumps(row["fields"])
        row["fields"] = json.loads(dict_str, object_pairs_hook=dict_clean)
        idcsvphc_datapointsnew.append(row["fields"])
    
    
    idcdomainhc_datapoints = json.loads(serialize("json", IDCDomainHeadcountV.objects.all()))
    idcdomainhc_datapointsnew = []
    for row in idcdomainhc_datapoints:
        dict_str = json.dumps(row["fields"])
        row["fields"] = json.loads(dict_str, object_pairs_hook=dict_clean)
        idcdomainhc_datapointsnew.append(row["fields"])


    idcdomhrs_datapoints = json.loads(serialize("json", IDCDomainHoursV.objects.all()))
    idcdomhrs_datapointsnew = []
    for row in idcdomhrs_datapoints:
        dict_str = json.dumps(row["fields"])
        row["fields"] = json.loads(dict_str, object_pairs_hook=dict_clean)
        idcdomhrs_datapointsnew.append(row["fields"])

    
    idcvphrs_datapoints = json.loads(serialize("json", IDCVPHoursV.objects.all()))
    idcvphrs_datapointsnew = []
    for row in idcvphrs_datapoints:
        dict_str = json.dumps(row["fields"])
        row["fields"] = json.loads(dict_str, object_pairs_hook=dict_clean)
        idcvphrs_datapointsnew.append(row["fields"])

    
    atsvenempvphc_datapoints = json.loads(serialize("json", ATSVPVendorEmpV.objects.all()))
    atsvenempvphc_datapointsnew = []
    for row in atsvenempvphc_datapoints:
        dict_str = json.dumps(row["fields"])
        row["fields"] = json.loads(dict_str, object_pairs_hook=dict_clean)
        atsvenempvphc_datapointsnew.append(row["fields"])

 
    atsvencondomhc_datapoints = json.loads(serialize("json", ATSDEPTVendorEmpV.objects.all()))
    atsvencondomhc_datapointsnew = []
    for row in atsvencondomhc_datapoints:
        dict_str = json.dumps(row["fields"])
        row["fields"] = json.loads(dict_str, object_pairs_hook=dict_clean)
        atsvencondomhc_datapointsnew.append(row["fields"])


    return render(request, 'index.html',{ "idcvphc_datapoints": idcsvphc_datapointsnew,  "idcvphrs_datapoints": idcvphrs_datapointsnew,"idcdomhc_datapoints": idcdomainhc_datapointsnew,"idcdomhrs_datapoints":idcdomhrs_datapointsnew,"atsvencondomhc_datapoints":atsvencondomhc_datapointsnew,"atsvenempvphc_datapoints":atsvenempvphc_datapointsnew,"idcschedulefinish_datapoints":idcschedulefinish_datapointsnew})                                        


def excelUpload(request):
    data = {}
    if "GET" == request.method:
	    return render(request, "excelUpload.html", data)
    # if not GET, then proceed
    try:
        csv_file = request.FILES["customFile"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("excelUpload"))
        #if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse("excelUpload"))
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = dir_path + "/static/"
        fs = FileSystemStorage(dir_path)
        filename = fs.save(csv_file.name, csv_file)  
        messages.success("File Upload SuccessFull" ,fs.url(filename))

    except Exception as e:
        messages.error(request,"Unable to upload file. "+repr(e))

    return HttpResponseRedirect(reverse("excelUpload"))