from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from.serializers import user,userserializer


class UserApi(ListCreateAPIView):
    serializer_class=userserializer
    queryset=user.objects.all()


from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(http_method_names=['GET','POST'])
def logoutf(request):
    logout(request)
    return Response(data={'message':'loged out'},status=status.HTTP_200_OK)
