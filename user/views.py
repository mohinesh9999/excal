from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
import math,random
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
# Create your views here.
def generateOTP(): 
    digits = "0123456789"
    OTP = "" 
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
    return OTP
def OTP(request,email1):
    # print((str(request.POST)),request.FILES) 
    q=User.objects.filter(email=email1)
    # q1=student3.objects.filter(user=q[0])[0]
    # print(q[0],len(q),q1.getv())
    if(len(q)!=0):
        return JsonResponse({'otp':'exist'})
    otp=generateOTP()
    send_mail('Verificaton for signup', otp, 'sihkkr2020@gmail.com', [email1])
    return JsonResponse({'otp':otp})
def OTP_fp(request,email1):
    # print((str(request.POST)),request.FILES) 
    q=User.objects.filter(email=email1)
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
    student3(user=user,name=x['name'],gender=x['gender']).save()
    return JsonResponse({'otp':'otp'})
@api_view(['POST'])
def FP(request):
    print(((request.data)))
    x=request.data
    u = User.objects.get(username=x['email'])
    u.set_password(x['password'])
    u.save()
    return JsonResponse({'otp':'otp'})