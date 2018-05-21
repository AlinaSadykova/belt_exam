from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
strongRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')


class UserManager(models.Manager):
    def basic_validator(self, postData):
        y = User.objects.filter(last_name = postData['last_name'])
        response =  {
            'status': False,
            'errors': [],
            'success':[]
        }
        
        if len(postData['first_name']) < 3:
            response['errors'].append("Name should be at least 3 characters") 
        if len(postData['last_name']) < 3:
            response['errors'].append("User name should be at least 3 characters") 
        if len(postData['password'])<8:
            response['errors'].append("Password is too short") 
        if  not strongRegex.match(postData['password']):
            response['errors'].append("Password must contain at least 1 uppercase character and number")
        if (postData['password'])!=(postData['confps']):
            response['errors'].append("Passwords don not match") 
        if len(y)>0:
            response['errors'].append("user already exists") 
        if len(response['errors'])==0:
            response['status']=True
            response['success'].append("You are successfully registered!")
        return response

    def validation2(self, postData):
        response =  {
            'status': False,
            'errors': []
        }
        y = User.objects.filter(last_name = postData['last_name'])
        if len(y)>0:
            if bcrypt.checkpw(postData['password'].encode(), y[0].password.encode()):
                response['errors'].append("you are successfully logged in")
                response['status'] = True
        else:
            response['errors'].append("you can not be logged in") 
        return response

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    startdate = models.DateTimeField(auto_now_add = False)
    enddate = models.DateTimeField(auto_now = False)
    
   


class User(models.Model):
    first_name = models.CharField(max_length=255)
    trips= models.ManyToManyField(Trip, related_name="users")
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()



