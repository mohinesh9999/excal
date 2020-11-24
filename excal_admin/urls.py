from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('addnoti/', addnoti.as_view(), name ='addnoti'),
    path('changepass/', changepass.as_view(), name ='changepass'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)