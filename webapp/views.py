from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import formModel
from .serializers import employeeSerializer
from django.views.generic import TemplateView,CreateView,ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import myForm
from django.utils.decorators import method_decorator
import json


# Create your views here.

class empList(APIView):
	def get(self,request):
		employees1 = formModel.objects.all()
		serializer = employeeSerializer(employees1,many=True)
		return Response(serializer.data)
	 	

	def post(self):
		pass


class CreatePatientForm(LoginRequiredMixin,CreateView):
	login_url = '/login/'
	template_name = 'webapp/createPatient.html'
	form_class = myForm
	success_url = 'webapp/stepOneModel_list.html'

class PatientsList(ListView):
	model = formModel
	paginate_by = 50

	def get_queryset(self):
		return formModel.objects.filter(Opno__isnull=False)


class ThankYouPage(TemplateView):
	template_name = 'webapp/thankyou.html'
