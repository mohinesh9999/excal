from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('sendotp/<str:email1>/',OTP),
    path('sendotp_fp/<str:email1>/',OTP_fp),
    path('signup/',signup.as_view(), name ='signup'),
    path('FP/',FP),
    path('addmentor/', addmentor.as_view(), name ='addmentor'),
    path('profile/', profile.as_view(), name ='profile'),
    path('buysell/', addbuysell.as_view(), name ='addbuysell'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)