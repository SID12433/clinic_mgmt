from rest_framework import serializers
from django.contrib.auth.models import User
from clinic.models import Doctor,Appointment


class UserCreationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','password','email']

    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields="__all__"

class AppointmentSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Appointment
        fields="__all__"
        
class AppointmentViewSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    doctor=DoctorSerializer()
    class Meta:
        model=Appointment
        fields="__all__"