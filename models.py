#from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



class Admission(models.Model):
   name = models.CharField(max_length=200, default="")
   email = models.EmailField(max_length=500, default="")
   dob = models.DateField(max_length=8)
   mobile_number = models.CharField(max_length=12)
   city  = models.CharField(max_length=100, default="")
   address  = models.CharField(max_length=100, default="")


   GENDER = (
       ('M', 'Male'),
       ('F', 'Female'),
       ('O', 'Other'),
   )

   gender = models.CharField(max_length=2, choices=GENDER)

   APPLIED_FOR = (
       ('B', 'B.Sc'),
       ('M', 'M.Sc'),
       ('M', 'M.Pharm'),
       ('L', 'Law & humanities'),
       ('BB', 'BBA'),
   )

   appiled_for = models.CharField(max_length=2, choices=APPLIED_FOR)


   def __str__(self):
     return self.name
   
class Contact(models.Model):
   name = models.CharField(max_length=100, default="")
   email = models.EmailField(max_length=500, default="")
   #admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
   message = models.CharField(max_length=100, default="")


   def __str__(self):
       return self.name