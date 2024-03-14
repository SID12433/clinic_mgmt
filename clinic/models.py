from django.contrib.auth.models import User
from django.db import models

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    speciality=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Appointment(models.Model):
    patient_name=models.CharField(max_length=100)
    age=models.IntegerField()
    appointment_date=models.DateField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)