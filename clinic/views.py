from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.decorators import action


from clinic.serializer import UserCreationSerializer,DoctorSerializer,AppointmentSerializer,AppointmentActionSerializer,AppointmentViewSerializer
from clinic.models import User,Doctor,Appointment


#this is the view for registration 
class UserCreateView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
       
        
#this is the view for view their profile       
class ProfileView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
      
    def get(self,request,*args,**kwargs):
        user_id=request.user.id
        print(user_id)
        qs=User.objects.get(id=user_id)
        serializer=UserCreationSerializer(qs)
        return Response(data=serializer.data)
    

#this is the view for listing available doctors    
class DoctorView(ViewSet):
    
    def list(self,request,*args,**kwargs):
        qs=Doctor.objects.all()
        serializer=DoctorSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Doctor.objects.get(id=id)
        serializer=DoctorSerializer(qs)
        return Response(data=serializer.data)
    
    
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    @action(methods=['post'],detail=True)
    def create_appointment(self,request,*args,**kwargs):
        serializer=AppointmentActionSerializer(data=request.data)
        user_id=request.user.id
        id=kwargs.get('pk')
        doctor_obj=Doctor.objects.get(id=id)
        user_obj=User.objects.get(id=user_id)
        if serializer.is_valid():
            serializer.save(user=user_obj,doctor=doctor_obj)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)  


        
        
#this is the view for listing users appointments     
class AppointmentView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def create(self,request,*args,**kwargs):
        serializer=AppointmentSerializer(data=request.data)
        user_id=request.user.id
        user_obj=User.objects.get(id=user_id)
        if serializer.is_valid():
            serializer.save(user=user_obj)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)    

    
    def list(self,request,*args,**kwargs):
        user_id=request.user.id
        user_obj=User.objects.get(id=user_id)
        qs=Appointment.objects.filter(user=user_obj)
        serializer=AppointmentViewSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Appointment.objects.get(id=id)
        serializer=AppointmentViewSerializer(qs)
        return Response(data=serializer.data)