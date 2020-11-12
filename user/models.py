from django.db import models
# import cloudinary
# from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class student3(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name=models.CharField(max_length=100,blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=False,null=False)
    def __str__(self):            
        return self.user.email

    def getv(self):
        return {'gender':self.gender,'email':self.user.email,'name':self.name,
                'password':self.user.password}
