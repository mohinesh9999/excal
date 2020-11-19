from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class student3(models.Model):
    email=models.EmailField(unique=True,primary_key=True)
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
class mentor(models.Model):
    email=models.EmailField(primary_key=True,unique=True)
    std=models.OneToOneField(student3, on_delete=models.CASCADE)
    branch=models.CharField(max_length=100,blank=False)
    year=models.CharField(max_length=100,blank=False)
    prog=models.CharField(max_length=100,blank=False)
    skills=models.TextField(blank=False)
    areaofinterest=models.TextField(blank=False)
    rollno=models.CharField(max_length=100,blank=False)
    image=CloudinaryField(blank=True, null=True)
    def getv(self):
        return {'skills':self.skills,
                'prog':self.prog,
                'year':self.year,
                'branch':self.branch,
                'areaofinterest':self.areaofinterest,
                'rollno':self.rollno,
                }
class buysell(models.Model):
    SHOW_CHOICES = (
        ('T', 'yes'),
        ('F', 'no'),
    )
    p_id = models.AutoField(primary_key=True)
    registered_at=models.DateTimeField(auto_now=True)
    std1=models.ForeignKey(student3, on_delete = models.CASCADE)
    std=models.ForeignKey(mentor, on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=100,blank=False)
    desc=models.TextField(blank=False)
    isshow=models.CharField(max_length=1, choices=SHOW_CHOICES,blank=False,null=False)
    image=CloudinaryField(blank=True, null=True)
    price=models.CharField(max_length=100,blank=False)
    def getv(self):
        return {'registered_at':self.registered_at,
                'pname':self.name,
                'desc':self.desc,
                'isshow':self.isshow,
                'price':self.price,
                }

