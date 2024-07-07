from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import CreateSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from accounts import models
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
# Create your views here.

class Logout(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    
class UserDelete(APIView):
    permission_classes = [IsAdminUser]
    def delete(self,request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class UserCreate(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, format=None):
        serializer = CreateSerializer(data=request.data)
        
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "User is created successfully !"
            data['username'] = account.username
            data['email'] = account.email
            
            token = Token.objects.get(user=account).key
            data['token'] = token
             
        else:
            data = serializer.errors
        return Response(data)