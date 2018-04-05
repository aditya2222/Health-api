from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import stepOneModel
from .serializers import employeeSerializer
from django.views.generic import TemplateView,CreateView,ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import myForm
# Create your views here.


class empList(APIView):
	def get(self,request):
		employees1 = stepOneModel.objects.all()
		serializer = employeeSerializer(employees1,many=True)
		return Response(serializer.data)
	 	

	def post(self):
		pass


class CreatePatientForm(LoginRequiredMixin,CreateView):
	login_url = '/login/'
	redirect_field_name = 'webap/steponemodel_list.html'
	template_name = 'webapp/createPatient.html'
	form_class = myForm


class PatientsList(ListView):
	model = stepOneModel
	paginate_by = 50

	def get_queryset(self):
		return stepOneModel.objects.all()


class ThankYouPage(TemplateView):
	template_name = 'webapp/thankyou.html'
