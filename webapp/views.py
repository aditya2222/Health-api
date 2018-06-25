from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework import status
from .models import formModel
from .serializers import patientSerializer
from django.views.generic import TemplateView,CreateView,ListView,TemplateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.renderers import StaticHTMLRenderer
from .forms import myForm
from django.utils.decorators import method_decorator
from reportlab.pdfgen import canvas
import reportlab.rl_config
import json


# Create your views here.

class empList(APIView):
	def get(self,request):
		employees1 = formModel.objects.all()
		serializer = employeeSerializer(employees1,many=True)
		return Response(serializer.data)
	 	

	def post(self):
		pass

class createPDFReport(APIView):
	def get(self,request):
		parameters = request.query_params
		kureid=parameters.get('kureid')
		print(kureid)
		c = canvas.Canvas("/Users/vyramach/Documents/Kure/MVP/source/mvp/pdfs/"+kureid+".pdf")
		c.drawString(100, 100,kureid)
		c.showPage()
		c.save()
		return Response(kureid)
	

class CreatePatientForm(LoginRequiredMixin,CreateView):
	login_url = '/login/'
	template_name = 'webapp/createPatient.html'
	form_class = myForm
	success_url = 'webapp/stepOneModel_list.html'
	reportlab.rl_config.warnOnMissingFontGlyphs = 0


class CreatePatientAutofilledForm(LoginRequiredMixin,CreateView):
	login_url = '/login/'
	template_name = 'webapp/createPatientautofill.html'
	form_class = myForm
	success_url = 'webapp/stepOneModel_list.html'
	reportlab.rl_config.warnOnMissingFontGlyphs = 0
	
#class dashboard(LoginRequiredMixin,APIView):
#	login_url='/login/'
#	def get(self,request):
#		return render(request, 'webapp/formmodel_list.html')


#@api_view(['GET'])
#@permission_classes((IsAuthenticated, ))
@login_required(login_url='/login/')
def dashboard(request, path=''):
    return render(request, 'webapp/formmodel_list.html')

class PatientsList(LoginRequiredMixin,APIView):
	login_url = '/login/'
	def get(self,request):
		patients=formModel.objects.all()
		serializer = patientSerializer(patients,many=True)
		return Response(serializer.data)
#class PatientsList(LoginRequiredMixin,ListView):
#	login_url='/login/'
#	model = formModel
#	paginate_by = 50
#
#	def get_queryset(self):
#		#print(formModel.objects)
#		return formModel.objects.filter(Opno__isnull=False)


class ThankYouPage(TemplateView):
	template_name = 'webapp/thankyou.html'


class PatientUpdate(UpdateView):
    model = formModel
    form_class = myForm
    template_name = 'webapp/editpatient.html'
    success_url = '/'
