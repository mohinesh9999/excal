from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
# Create your models here.
class noti(models.Model):
    p_id = models.AutoField(primary_key=True)
    theme=models.CharField(max_length=100,blank=False)
    desc=models.TextField(blank=False)
    registered_at=models.DateTimeField(auto_now=True)
    FILE=CloudinaryField(blank=True, null=True)

    def getv(self):
        return {'p_id':self.p_id,
                'theme':self.theme,
                'desc':self.desc,
                'registered_at':self.registered_at,
                'FILE':str(self.FILE)}