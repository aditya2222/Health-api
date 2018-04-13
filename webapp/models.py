from django.db import models
from django.utils.crypto import get_random_string
from mongoengine import *

connect('appDB')
# Create your models here.

class formModel(models.Model):
	Name = models.CharField(max_length=120,default="Unnamed")
	Age = models.IntegerField(default=0,blank=True)
	genderChoice = models.CharField(max_length=10,null=True,blank=True)
	Opno = models.IntegerField(default=0,blank=True)
	Ipno = models.IntegerField(default=0,blank=True)
	Address = models.TextField(null=True,blank=True)
	Phoneno = models.IntegerField(blank=True)
	Kureid = models.CharField(max_length=120,blank=True,null=True)
	ChiefComplaints = models.CharField(max_length=120,null=True,blank=True)
	Historyofillness = models.CharField(max_length=120,null=True,blank=True)
	PastHistory = models.CharField(max_length=150,blank=True,null=True)
	FamilyHistory = models.CharField(max_length=150,blank=True,null=True)
	ProvisionalDiagnosis = models.CharField(max_length=150,blank=True,null=True)
	Medicationhistroy = models.CharField(max_length=120,null=True,blank=True)
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







