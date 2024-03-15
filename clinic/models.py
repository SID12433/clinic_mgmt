from django.contrib.auth.models import User
from django.db import models

class Doctor(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    speciality=models.CharField(max_length=100,blank=False,null=False)
    department=models.CharField(max_length=100,blank=False,null=False)
    
    def __str__(self):
        return self.name
    
    
class Appointment(models.Model):
    patient_name=models.CharField(max_length=100,blank=False,null=False)
    age=models.IntegerField(blank=False,null=False)
    appointment_date=models.DateField(blank=False,null=False)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,blank=False,null=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)