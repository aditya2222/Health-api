from django.db import models

# Create your models here.

class stepOneModel(models.Model):
	fullName = models.CharField(max_length=10)
	emailAddress = models.EmailField()
	contact = models.IntegerField()
	comEmail = models.BooleanField(default=False)
	comSms = models.BooleanField(default=False)
	comPhone = models.BooleanField(default=False)
	payCreditCard = models.BooleanField(default=False)
	payBitCoin = models.BooleanField(default=False)
	payCash = models.BooleanField(default=False)
	amount = models.CharField(max_length=10)

	def __str__(self):
		return self.fullName




