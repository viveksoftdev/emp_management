from django.db import models
import json

# Model for employee

class Employee(models.Model):
    GENDER_CHOICES = (('M','MALE')
                      ,('F','FEMALE'),
                      ('O','OTHER'))
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15,blank=True)
    address = models.TextField(default=json.dumps({}))
    workExp =  models.TextField(default=json.dumps({}))
    qualifications = models.TextField(default=json.dumps({}))











