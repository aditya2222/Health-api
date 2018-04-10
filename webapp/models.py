from django.db import models
from django.utils.crypto import get_random_string
from mongoengine import *

connect('appDB')
# Create your models here.

class formModel(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	Name = models.CharField(max_length=120,default="Unnamed")
	Age = models.IntegerField(default=0,blank=True)
	genderChoice = models.CharField(max_length=10,null=True,blank=True,choices=GENDER_CHOICES)
	Opno = models.IntegerField(default=0,blank=True)
	Ipno = models.IntegerField(default=0,blank=True)
	Address = models.TextField(null=True,blank=True)
	Phoneno = models.IntegerField(default=0,blank=True)
	Kureid = models.CharField(max_length=120,default=get_random_string(length=32))
	ChiefComplaints = models.CharField(max_length=120,null=True,blank=True)
	Historyofillness = models.TextField(null=True,blank=True)
	PastHistory = models.TextField(null=True,blank=True)
	Familyhistory = models.TextField(null=True,blank=True)
	Medicationhistroy = models.TextField(null=True,blank=True)
	Alcohol = models.BooleanField(default=False,blank=True)
	Smoking = models.BooleanField(default=False,blank=True)
	Bowel = models.BooleanField(default=False,blank=True)
	Bladder = models.BooleanField(default=False,blank=True)
	Sleep = models.BooleanField(default=False,blank=True)
	Summary = models.TextField(null=True,blank=True)
	Examinedby = models.CharField(max_length=10,null=True,blank=True)
	Verifiedby = models.CharField(max_length=10,null=True,blank=True)


	def __str__(self):
		return self.Name

class newModel(models.Model):
	name = models.CharField(max_length=120)




