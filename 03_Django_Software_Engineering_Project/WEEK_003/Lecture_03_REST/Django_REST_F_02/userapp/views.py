from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.views import APIView
from userapp.serializers import RegistrationSerializer
from userapp.signals import *
# Create your views here.
class RegistrationView(APIView):
    def post(self, request):
        data={}
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account=serializer.save()
            data['response']='Registration successful'
            data['username']=account.username
            data['email']=account.email
            token=Token.objects.get(user=account).key
            data['token']=token
        else:
            data=serializer.errors
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LogoutView(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)