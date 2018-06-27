from django.urls import path
from .views import CreatePatientForm,PatientsList,createPDFReport,dashboard,CreatePatientAutofilledForm,PatientUpdate,GeneratePDF


urlpatterns = [
path('createpatient/',CreatePatientForm.as_view(success_url="/"),name='createpatient'),
path('updatepatient/<int:pk>/',PatientUpdate.as_view(),name='updatepatient'),
path('createpatientautfill/',CreatePatientAutofilledForm.as_view(success_url="/"),name='createpatientautofilled'),
path('generatepdf/<int:pk>',GeneratePDF.as_view(),name='GeneratePDF'),
path('getpatients/',PatientsList.as_view(),name='createPDF'),
path('',dashboard,name='dashboard'),
]