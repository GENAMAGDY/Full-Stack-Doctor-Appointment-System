from  rest_framework import serializers
from DoctorApp.models import Doctor, Patient

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields = ('DoctorID',
                    'DoctorFirstName',
                    'DoctorLastName',
                    'DoctorUserName',
                    'DoctorEmail',
                    'DoctorPassword')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields = ('PatientID', 
                   'Doctor_ID',
                   'PatientFirstName',
                   'PatientLastName',
                   'PatientUserName',
                   'PatientEmail',
                   'PatientPassword',
                   'blood_pressure',
                   'medications',
                   'image')
           

 
