from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
import math,random
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
import  cloudinary
class viewnoti(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        l=[]
        w=noti.objects.all()
        for i in w:
            print(cloudinary.utils.cloudinary_url(str(i.FILE)))
            l.append(i.getv())
        l.sort(key=lambda x:(x['registered_at']))
        l=l[::-1]
        return JsonResponse({'result':l})
class addnoti(APIView): 
    permission_classes = (IsAdminUser, )
    def post(self,request):
        x=request.data
        noti(theme=x['theme'],
            desc=x['desc'],
            FILE=x['FILE'],
            ).save()
        return JsonResponse({'result':'done'})
class changepass(APIView):
    permission_classes = (IsAdminUser, )
    def post(self,request):
        x=request.data
        u = User.objects.get(username=request.user.email)
        u.set_password(x['password'])
        u.save()
        return JsonResponse({'otp':'otp'})