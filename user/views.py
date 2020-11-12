from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
import math,random
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def generateOTP(): 
    digits = "0123456789"
    OTP = "" 
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
    return OTP
def OTP(request,email1):
    # print((str(request.POST)),request.FILES) 
    q=student3.objects.filter(pk=email1)
    if(len(q)!=0):
        return JsonResponse({'otp':'exist'})
    otp=generateOTP()
    send_mail('Verificaton for signup', otp, 'sihkkr2020@gmail.com', [email1])
    return JsonResponse({'otp':otp})
def OTP_fp(request,email1):
    # print((str(request.POST)),request.FILES) 
    q=student3.objects.filter(pk=email1)
    # print(q[0].getv(),len(q))
    if(len(q)==0):
        return JsonResponse({'otp':'not exist'})
    otp=generateOTP()
    send_mail('Verificaton for signup', otp, 'sihkkr2020@gmail.com', [email1])
    return JsonResponse({'otp':otp})
from django.views.decorators.csrf import csrf_exempt
@api_view(['POST'])
def signup(request):
    print(((request.data)))
    x=request.data
    user=User.objects.create_user(x['email'], x['email'], x['password'])
    user.is_active=True
    user.save()
    user = User.objects.get(username=x['email'])
    student3(user=user,email=x['email'],name=x['name'],gender=x['gender']).save()
    return JsonResponse({'otp':'otp'})
@api_view(['POST'])
def FP(request):
    print(((request.data)))
    x=request.data
    u = User.objects.get(username=x['email'])
    u.set_password(x['password'])
    u.save()
    return JsonResponse({'otp':'otp'})
class addmentor(APIView): 
    permission_classes = (IsAuthenticated, ) 
    def get(self,request):
        l=[]
        w=mentor.objects.all()
        print(w)
        for i in w:
            d=i.getv()
            d['image']=str(i.image)
            d.update(i.std.getv())
            print(d)
            # del d['std']
            l.append(d)
        return JsonResponse({'result':l})
    def post(self, request): 
        print(request.user,request.data)
        x=request.data
        w=student3.objects.filter(pk=request.user.email)
        mentor(
            std=w[0],
            email=request.user.email,
            prog=x['prog'],
            areaofinterest=x['areaofinterest'],
            year=x['year'],
            branch=x['branch'],
            rollno=x['rollno'],
            skills=x['skills'],
            image=x['image']
        ).save()
        return JsonResponse({'otp':'otp'})
class profile(APIView): 
    permission_classes = (IsAuthenticated, ) 
    def get(self,request):
        d1=student3.objects.filter(pk=request.user.email)[0].getv()
        print(d1)
        x=mentor.objects.filter(pk=request.user.email)
        # print(str(x[0].image))
        d2=dict()
        if(len(x)==1):
            d2=x[0].getv()
            d2['image']=str(x[0].image)
        d1.update(d2)
        return JsonResponse({'result':d1})
    