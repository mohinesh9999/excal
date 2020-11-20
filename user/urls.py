from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('signup/',signup.as_view(), name ='signup'),
    path('sendotp/<str:email1>/',OTP),
    path('sendotp_fp/<str:email1>/',OTP_fp),
    path('FP/',FP.as_view(), name ='FP'),
    path('profile/', profile.as_view(), name ='profile'),
    path('addmentor/', addmentor.as_view(), name ='addmentor'),
    path('buysell/', addbuysell.as_view(), name ='addbuysell'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)