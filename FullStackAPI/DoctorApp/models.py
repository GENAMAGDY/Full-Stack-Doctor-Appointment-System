from django.db import models

# Create your models here.
class Doctor(models.Model):
    DoctorID = models.AutoField(primary_key = True)
    DoctorFirstName = models.CharField(max_length = 50)
    DoctorLastName= models.CharField(max_length = 50)
    DoctorUserName= models.CharField(max_length = 100)
    DoctorEmail= models.EmailField()
    DoctorPassword= models.CharField(max_length = 100)


class Patient(models.Model):
    PatientID = models.AutoField(primary_key = True)
    Doctor_ID = models.IntegerField()
    PatientFirstName = models.CharField(max_length = 50)
    PatientLastName= models.CharField(max_length = 50)
    PatientUserName= models.CharField(max_length = 100)
    PatientEmail= models.EmailField()
    PatientPassword= models.CharField(max_length = 100)
    blood_pressure = models.CharField(null=True, max_length = 20)
    medications = models.TextField(null=True)
    image = models.ImageField(null =True)
    