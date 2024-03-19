from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from .manager import UserManager


  
# Create your models here.
class Teacher(models.Model):
     full_name=models.CharField(max_length=100)
     email=models.CharField(max_length=100)
     password=models.CharField(max_length=100)
     mobile_no=models.CharField(max_length=20)

     #course category model
class gamecategory(models.Model):
     title=models.CharField(max_length=150)
     description=models.CharField(max_length=100)
   
#student model    
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    otp = models.CharField(max_length=6, blank=True, null=True)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    college_year = models.IntegerField(null=True, blank=True)
    email_verified = models.BooleanField(default= False)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.email  
    
# timeline model
class Timeline(models.Model):
    time = models.DateTimeField()
    description = models.TextField()
    gamename = models.CharField(max_length=200) 

    def __str__(self):
        return self.description    

 #game
class Game(models.Model):
    game_name = models.CharField(max_length=100)
    game_details = models.TextField()
    game_image = models.ImageField(upload_to='games/', blank=True, null=True)

    def __str__(self):
        return self.game_name 
           
#registration
class Usersregistration(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)     
