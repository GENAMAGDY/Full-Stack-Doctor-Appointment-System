from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from DoctorApp.models import Doctor, Patient
from DoctorApp.Serializers import DoctorSerializer, PatientSerializer
from django.core.files.storage import default_storage
import pytesseract
import os
import tempfile
import subprocess
from django.conf import settings
import pytesseract
from django.shortcuts import render

#pip install pytesseract
# Create your views here.
from django.core.mail import send_mail

@csrf_exempt
def DoctorApi(request, id=0):
    if request.method =='GET':
        Doctors = Doctor.objects.all()
        Doctors_Serializer = DoctorSerializer(Doctors, many=True)
        return JsonResponse(Doctors_Serializer.data, safe=False)
    elif request.method =='POST':
        Doctors = JSONParser().parse(request)
        Doctors_Serializer = DoctorSerializer(data=Doctors)
        if Doctors_Serializer.is_valid():
            Doctors_Serializer.save()
            return JsonResponse("Added Successful!",safe=False)
        return JsonResponse("Failed to Add!",safe=False)
    elif request.method =='PUT':
        Doctor_data = JSONParser().parse(request)
        Doctor_1 = Doctor.objects.get(DoctorID=Doctor_data['DoctorID'])
        Doctor_Serializer=DoctorSerializer(Doctor_1 , data =Doctor_data)
        if Doctor_Serializer.is_valid():
            Doctor_Serializer.save()
            return JsonResponse("Update Successful!",safe=False)
        return JsonResponse("Failed to Update!",safe=False)
@csrf_exempt
def PatientApi(request, id=0):
    if request.method =='GET':
        Patients = Patient.objects.all()
        Patients_Serializer = PatientSerializer(Patients, many=True)
        return JsonResponse(Patients_Serializer.data, safe=False)
    elif request.method =='POST':
        Patients = JSONParser().parse(request)
        Patients_Serializer = PatientSerializer(data=Patients)
        if Patients_Serializer.is_valid():
            Patients_Serializer.save()
            return JsonResponse("Added Successful!",safe=False)
        return JsonResponse("Failed to Update!",safe=False)
    elif request.method =='PUT':
        Patient_data = JSONParser().parse(request)
        Patient_1 = Patient.objects.get(PatientID=Patient_data['PatientID'])
        Patient_Serializer=PatientSerializer(Patient_1 , data =Patient_data)
        if Patient_Serializer.is_valid():
            Patient_Serializer.save()
            return JsonResponse("Update Successful!",safe=False)
        return JsonResponse("Failed to Update!",safe=False)


        
@csrf_exempt
def SendEmailPatient(request):
    if request.method=='POST':
        Patient_data = JSONParser().parse(request)
        Patientdata = Patient.objects.get(PatientEmail=Patient_data['PatientEmail'])
        Patient_Serializer = PatientSerializer(Patientdata)
       
        # Build Email
        
        sub="Doctor Website"
        message= "Dear Sir,\n I hope you are well. Your password is "+ str(Patient_Serializer.data['PatientPassword'])+"\n Regards"
        to = Patient_Serializer.data['PatientEmail']
        send_mail(sub,message,settings.EMAIL_HOST_USER,[to],fail_silently=False)
        
        return JsonResponse("Successful!",safe=False)
    return JsonResponse("Failed!",safe=False)

@csrf_exempt
def SendEmailDoctor(request):
    if request.method=='POST':
        Doctor_data = JSONParser().parse(request)
        Doctordata = Doctor.objects.get(DoctorEmail=Doctor_data['DoctorEmail'])
        Doctor_Serializer = DoctorSerializer(Doctordata)
       
        # Build Email
        
        sub="Doctor Website"
        message= "Dear Sir,\n I hope you are well. Your password is "+ str(Doctor_Serializer.data['DoctorPassword'])+"\n Regards"
        to = Doctor_Serializer.data['DoctorEmail']
        send_mail(sub,message,settings.EMAIL_HOST_USER,[to],fail_silently=False)
        
        return JsonResponse("Successful!",safe=False)
    return JsonResponse("Failed!",safe=False)
        
    


       


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadFile']
    file_name = default_storage.save(file.name,file)
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

    return JsonResponse(pytesseract.image_to_string('media/'+file_name),safe=False)

