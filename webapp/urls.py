from django.urls import path
from .views import CreatePatientForm,PatientsList,createPDFReport,dashboard,CreatePatientAutofilledForm


urlpatterns = [
path('createpatient/',CreatePatientForm.as_view(success_url="/"),name='createpatient'),
path('createpatientautfill/',CreatePatientAutofilledForm.as_view(success_url="/"),name='createpatientautofilled'),
path('createpdf/',createPDFReport.as_view(),name='createPDF'),
path('getpatients/',PatientsList.as_view(),name='createPDF'),
path('',dashboard,name='dashboard'),
]