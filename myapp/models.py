# from django.db import models

# # Create your models here.

# class sos2(models.Model):
#     La = models.TextField()

#     def __str__(self):
#         return self.La
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class sos2(models.Model):

    La = models.CharField(max_length=100)
    Fp = models.CharField(max_length=100,default="")
    Sn = models.CharField(max_length=100,default="")
    Ws = models.CharField(max_length=100,default="")
    Ca = models.CharField(max_length=100,default="")

    def _str_(self):
        return f"{self.La} {self.Fp} {self.Sn} {self.Ws} {self.Ca}"
    
class so1(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    La = models.CharField(max_length=100)
    Fp = models.CharField(max_length=100,default="")
    Sn = models.CharField(max_length=100,default="")
    Ws = models.CharField(max_length=100,default="")
    Ca = models.CharField(max_length=100,default="")

    def _str_(self):
        return f"{self.La} {self.Fp} {self.Sn} {self.Ws} {self.Ca}"
