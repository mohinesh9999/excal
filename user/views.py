from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
import math,random
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,AllowAny
import cloudinary
import hashlib
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
    send_mail('Verificaton for signup', "otp for verification is "+str(otp), 'sihkkr2020@gmail.com', [email1])
    return JsonResponse({'otp':hashlib.md5((str(otp)).encode()).hexdigest()})
def OTP_fp(request,email1):
    # print((str(request.POST)),request.FILES) 
    q=student3.objects.filter(pk=email1)
    # print(q[0].getv(),len(q))
    if(len(q)==0):
        return JsonResponse({'otp':'not exist'})
    otp=generateOTP()
    send_mail('Verificaton for forgot password', "otp for verification is "+str(otp), 'sihkkr2020@gmail.com', [email1])
    return JsonResponse({'otp':hashlib.md5((str(otp)).encode()).hexdigest()})
# @api_view(['POST'])
# def signup(request):
#     print(((request.data)))
#     x=request.data
#     user=User.objects.create_user(x['email'], x['email'], x['password'])
#     user.is_active=True
#     user.save()
#     user = User.objects.get(username=x['email'])
#     student3(user=user,email=x['email'],name=x['name'],gender=x['gender']).save()
#     return JsonResponse({'otp':'otp'})
class signup(APIView): 
    permission_classes = (AllowAny, ) 
    def post(self, request): 
        x=request.data
        user=User.objects.create_user(x['email'], x['email'], x['password'])
        user.is_active=True
        user.save()
        user = User.objects.get(username=x['email'])
        student3(user=user,email=x['email'],name=x['name'],gender=x['gender']).save()
        return JsonResponse({'otp':'otp'})
class FP(APIView): 
    permission_classes = (AllowAny, ) 
    def post(self, request): 
        print(((request.data)))
        x=request.data
        u = User.objects.get(username=x['email'])
        u.set_password(x['password'])
        u.save()
        return JsonResponse({'otp':'otp'})
from django.views.decorators.csrf import csrf_exempt
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
        y=buysell.objects.filter(std1=student3.objects.filter(pk=request.user.email)[0])
        l=[]
        for i in y:
            m=i.getv()
            m['image']=str(i.image)
            l.append(m)
        d2=dict()
        if(len(x)==1):
            d2=x[0].getv()
            d2['image']=str(x[0].image)
        d1.update(d2)
        return JsonResponse({'result':d1,'products':l})
class addbuysell(APIView): 
    permission_classes = (IsAuthenticated, ) 
    def get(self,request):
        l=[]
        w=buysell.objects.all()
        print(w)
        for i in w:
            d=i.getv()
            # print(type(i.image),(i.image).metadata())
            # print(cloudinary.utils.cloudinary_url(str(i.image)))
            d['pimage']=str(i.image)
            d.update(i.std1.getv())
            try:
                d.update(i.std.getv())
                d['image']=str(i.std.image)
            except:
                pass
            # del d['std']
            l.append(d)
        return JsonResponse({'result':l})
    def post(self,request):
        x=request.data
        w=mentor.objects.filter(pk=request.user.email)
        y=student3.objects.filter(pk=request.user.email)
        if(len(w)==0):
            w=None
        else:
            w=w[0]
        if(len(y)==0):
            y=None
        else:
            y=y[0]
        buysell(
            std1=y,
            std=w,
            name=x['name'],
            desc=x['desc'],
            isshow=x['isshow'],
            image=x['image'],
            price=x['price']
        ).save()
        return JsonResponse({'otp':'otp'})
    def put(self,request):
        b=buysell.objects.filter(pk=request.data['p_id']).update(isshow='F')
        return JsonResponse({'otp':'otp'})