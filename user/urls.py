from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('sendotp/<str:email1>/',OTP),
    path('sendotp_fp/<str:email1>/',OTP_fp),
    path('signup/',signup),
    path('FP/',FP),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)