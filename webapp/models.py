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
	PastHistory0 = models.CharField(max_length=120,null=True,blank=True,name="[0][PastHistory]")
	PastHistory1 = models.CharField(max_length=120,null=True,blank=True,name="[1][PastHistory]")
	PastHistory2 = models.CharField(max_length=120,null=True,blank=True,name="[2][PastHistory]")
	PastHistory3 = models.CharField(max_length=120,null=True,blank=True,name="[3][PastHistory]")
	PastHistory4 = models.CharField(max_length=120,null=True,blank=True,name="[4][PastHistory]")
	PastHistory5 = models.CharField(max_length=120,null=True,blank=True,name="[5][PastHistory]")
	PastHistory6 = models.CharField(max_length=120,null=True,blank=True,name="[6][PastHistory]")
	PastHistory7 = models.CharField(max_length=120,null=True,blank=True,name="[7][PastHistory]")
	PastHistory8 = models.CharField(max_length=120,null=True,blank=True,name="[8][PastHistory]")
	PastHistory9 = models.CharField(max_length=120,null=True,blank=True,name="[9][PastHistory]")
	PastHistor10 = models.CharField(max_length=120,null=True,blank=True,name="[10][PastHistory]")
	FamilyHistory0 = models.CharField(max_length=120,null=True,blank=True,name="[0][FamilyHistory]")
	FamilyHistory1 = models.CharField(max_length=120,null=True,blank=True,name="[1][FamilyHistory]")
	FamilyHistory2 = models.CharField(max_length=120,null=True,blank=True,name="[2][FamilyHistory]")
	FamilyHistory3 = models.CharField(max_length=120,null=True,blank=True,name="[3][FamilyHistory]")
	FamilyHistory4 = models.CharField(max_length=120,null=True,blank=True,name="[4][FamilyHistory]")
	FamilyHistory5 = models.CharField(max_length=120,null=True,blank=True,name="[5][FamilyHistory]")
	FamilyHistory6 = models.CharField(max_length=120,null=True,blank=True,name="[6][FamilyHistory]")
	FamilyHistory7 = models.CharField(max_length=120,null=True,blank=True,name="[7][FamilyHistory]")
	FamilyHistory8 = models.CharField(max_length=120,null=True,blank=True,name="[8][FamilyHistory]")
	FamilyHistory9 = models.CharField(max_length=120,null=True,blank=True,name="[9][FamilyHistory]")
	FamilyHistory10 = models.CharField(max_length=120,null=True,blank=True,name="[10][FamilyHistory]")
	ProvisionalDiagnosis = models.CharField(max_length=150,blank=True,null=True)
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






