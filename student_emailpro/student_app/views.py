from django.shortcuts import render
from rest_framework import viewsets
from rest_framework .response import Response
from rest_framework import status
from .serializers import StudentSerializer
from . models import StudentM
from django.shortcuts import get_object_or_404

from django.core.mail import send_mail
from django.conf import settings


class StudentViewset(viewsets.ViewSet):
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            val=(request.data)
            m=val['email']
            print(m)
            nm=val['fname']
            print(nm)

            subject='Welcome'
            message=f'Hey {nm}.... Welcome!! Thankyou For Registration'
            recipient_list=[m]
            from_mail=settings.EMAIL_HOST_USER
            send_mail(subject,message,from_mail,recipient_list)

            
            
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def list(self,request):
        Students=StudentM.objects.all()
        serializer=StudentSerializer(Students, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    

    def retrieve(self,request,pk=None):
        Students=get_object_or_404(StudentM,pk=pk)
        serializer=StudentSerializer(Students)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def update(self,request,pk=None):
        Students=get_object_or_404(StudentM,pk=pk)
        serializer=StudentSerializer(data=request.data, instance=Students)
        if serializer.is_valid():
             serializer.save()
             val=(request.data)
             m=val['email']
             print(m)
             nm=val['fname']
             print(nm)

             subject='Welcome'
             message=f'hey {nm}.... your data has been updated successfuly..'
             recipient_list=[m]
             from_mail=settings.EMAIL_HOST_USER
             send_mail(subject,message,from_mail,recipient_list)
             return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk=None):
        Students=get_object_or_404(StudentM,pk=pk)
        serializer=StudentSerializer(data=request.data,instance=Students,partial=True)
        if serializer.is_valid():
             serializer.save()
             val=(request.data)
             m=val['email']
             print(m)
             nm=val['fname']
             print(nm)

             subject='Welcome'
             message=f'hey {nm}.... Welcome!! Thankyou For Registration'
             recipient_list=[m]
             from_mail=settings.EMAIL_HOST_USER
             send_mail(subject,message,from_mail,recipient_list)
             return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        Students=get_object_or_404(StudentM,pk=pk)
        Students.delete()
        return Response(data=None,status=status.HTTP_204_NO_CONTENT)
    


    
    
    

